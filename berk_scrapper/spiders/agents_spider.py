import scrapy
from scrapy_playwright.page import PageMethod


class BerkSpiderSpider(scrapy.Spider):
    name = "berk_spider"
    
    def start_requests(self):
        # Initial request to get the agent list
        yield scrapy.Request('https://www.bhhsamb.com/roster/Agents', 
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_coroutines=[
                    PageMethod('wait_for_selector', 'div#rosterResults')  # Ensure the roster is loaded

                ]
            )
        )

    async def parse(self, response):
        # Loop through each agent and get their bio URL
        for agent in response.css('div#rosterResults article'):
            agent_url = agent.css('a::attr(href)').get()
            full_agent_url = response.urljoin(agent_url)  # Construct full URL
            
            # Make a new request to each agent's bio page
            yield scrapy.Request(full_agent_url, callback=self.parse_agent_details,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_coroutines=[
                        # Wait for the main profile section to load before scraping
                        PageMethod('wait_for_selector', 'rng-agent-profile-main'),
                    ]
                )
            )

    async def parse_agent_details(self, response):
        # Extract the required elements from the agent's profile page
        agent_name = response.css('.rng-agent-profile-contact-name::text').get(default='').strip()
        job_title = response.css('.rng-agent-profile-contact-title::text').get(default='').strip()
        
        # Extract phone number from the <li> element
        phone = response.css('.rng-agent-profile-contact-phone a::text').get(default='').strip()
        
        website = response.css('.rng-agent-profile-contact-website a::attr(href)').get(default='').strip()
        
        # Get the contact page link
        email_contact_page = response.css('.rng-agent-profile-contact-email a::attr(href)').get(default='').strip()
        email_contact_page = f"https://www.bhhsamb.com{email_contact_page}" if email_contact_page else None
        
        # Extract address from <li> element, handling both <strong> and outside text
        address_line_1 = response.css('.rng-agent-profile-contact-address strong::text').get(default='').strip()
        address_line_2 = response.css('.rng-agent-profile-contact-address::text').getall()[-1].strip() if response.css('.rng-agent-profile-contact-address::text').getall() else ''
        
        # Combine address lines into a full address
        full_address = f"{address_line_1} {address_line_2}".strip() if address_line_1 or address_line_2 else None

        # Extract profile image URL
        profile_image_url = response.css('.rng-agent-profile-main img::attr(src)').get(default='').strip()

        # Yield the cleaned data for each agent, with keys in a sensible order
        yield {
            'url': response.url,
            'name': agent_name,
            'job_title': job_title,
            'phone': phone,
            'contact_page': email_contact_page, 
            'website': website,
            'address': full_address,
            'profile_image_url': profile_image_url
        }
