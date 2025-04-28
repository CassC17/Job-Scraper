import scrapy
from job_scraper.items import JobScraperItem
import pathlib

class JobSpider(scrapy.Spider):
    name = "jobs-css"
    allowed_domains = ["lesjeudis.com"]
    start_urls = [ f"https://lesjeudis.com/jobs?page={i}&limit=50" for i in range(5)]

    def parse(self, response):
        job_cards = response.css("div.BaseJobCard_root__9JrMV") 
        
        for card in job_cards:
            link_relative = card.css("a::attr(href)").get()
            if link_relative:
                 link_absolute = response.urljoin(link_relative)
                 yield scrapy.Request(
                    url=link_absolute,
                    callback=self.parse_detail
                )

    def parse_detail(self, response):
        item = JobScraperItem()    
        item["title"] = response.css("div[data-testid='job-title']::text").get(default="Titre non trouvé")

        # precise description of the job mission
        mission_section = []
        capture = False
        all_elements = response.css("div[data-testid='html-renderer-job-main-body-text'] > *")

        for element in all_elements:
            tag_name = element.root.tag
            text = element.css("::text").get(default="").strip()

            if not text:
                continue

            if "Job Description" in text:
                capture = True
                continue

            if capture:
                if tag_name == "b" and text == "Qualifications":
                    break
                mission_section.append(text)
        item["description"] = " ".join(mission_section) if mission_section else "Mission non trouvée"
    
        item["company"] = response.css("a[data-testid='job-card-company-name-link']::text").get(default="Entreprise inconnue")

        detail_links = response.css("div[data-testid='job-detail-section'] a")
        location = None
        contract_type = None
        for link in detail_links:
            href = link.attrib.get("href", "")
            text = link.css("::text").get(default="").strip()
            if "occupationType=" in href:
                contract_type = text
            else:
                location = text
        item["location"] = location if location else "Localisation inconnue"
        item["contract_type"] = contract_type if contract_type else "Type de contrat inconnu"

        item["date_posted"] = response.css("div.JobDetail_mobileValue__DLlav::text").get(default="Date inconnue").strip()
        
        item["link"] = response.url
        yield item

        
        
        
        