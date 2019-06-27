from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from bs4 import BeautifulSoup as sp
import time
from bs4 import BeautifulSoup as soup
import ssl
import traceback
import shutil
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

import urllib.request

import pandas as pd
import json
import argparse
from pymongo import MongoClient
import json
from spiderapp.forms import HomePage

COMPANY_LIST = dict()
# Create your views here.

class HomePageView(TemplateView):

	def __init__(self):
		

	#Adding hosting addres to the carrier page 

		self.ebags='https://www.ebags.com'
		self.aetna='/search-jobs'

		self.lovesac='https://www.lovesac.com'
		self.rhone='https://www.rhone.com'
		self.altria='?src=leftnav'
		self.altria_1='http://www.altria.com'
		self.dell='https://jobs.delltechnologies.com'
		self.tableau='https://careers.tableau.com'

		self.arin='https://www.arin.net'

		self.accenture='https://www.accenture.com'
		self.jpcycles='https://www.jpcycles.com'

		self.gigaom='https://gigaom.com'

		self.zoomcare='https://www.zoomcare.com'

		self.walmart='https://careers.walmart.com'

		self.hsn='https://jobs.hsn.com'
		self.irs ='https://www.jobs.irs.gov'

		self.thinkchamp='http://www.thinkchamplin.com'

		self.lyondell='https://careers.lyondellbasell.com'
		self.lpl='https://careers.lpl.com'
		self.sbarro='https://sbarro.jobs.net'
		self.newscrop='https://newscorp.com'
		self.key='https://www.key.com'

		self.disney='https://jobs.disneycareers.com'

		self.warnermedia='https://www.att.jobs/'

		self.verizon='https://www.verizon.com'

		self.tapestry ='https://careers.tapestry.com'

		self.iac='https://www.iac.com'

		self.startribune='https://jobs.startribune.com'

		self.masco='https://jobs.masco.com'
		self.lazboy='http://jobs.jobvite.com'

		self.jiffymix='https://site.jiffymix.com/'

		self.spartanmash='https://careers.spartannash.com'

		self.starrett='http://www.starrett.com'

		self.manulife='https://jobs.manulife.com'

		self.fidelity='https://jobs.fidelity.com'

		self.yum='https://www.yum.com'

		self.rjcorman='https://wfa.kronostm.com/index.jsp'

		self.lexmark='https://www.lexmark.com'

		self.heavenhill='http://www.heavenhill.com'

		self.moback ='https://www.moback.com'
	#passing the job portal id's

	Jobportal_initials  = {
	    'tdxcorp': {
	        'search_link'     : 'https://www.tdxcorp.com',
	        'scrap_params': {
	                        'carrier_page_1'      : '#mega-menu-item-754',
	                        'title'               :  None,
	                        'carrier_page_2'      :  None
	                        }
	                    },    
	        
	      'ebags': {
	        'search_link'     : 'https://www.ebags.com',
	        'scrap_params': {
	                        'carrier_page_1'      : '#footerCICareers',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },     
	        'gartner': {
	        'search_link'     : 'https://www.gartner.com/en',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div.emt-container > footer > section > div > div.row.mg-t30.mg-b30 > div:nth-child(1) > ul > li:nth-child(2) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },  
	       
	        'lovesac': {
	        'search_link'     : 'https://www.lovesac.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#page-container > footer > section > div.bpc-nav-links.footer-group-1 > a:nth-child(3)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'rhone': {
	        'search_link'     : 'https://www.rhone.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : 'div.global_footer-section-list:nth-child(1) > a:nth-child(4)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'ediblearrangements': {
	        'search_link'     : 'https://www.ediblearrangements.com/edible-careers/edible-arrangements-careers',
	        'scrap_params': {
	                        'carrier_page_1'      : 'div.brnButton',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'altria': {
	        'search_link'     : 'http://www.altria.com/people-and-careers/training/Pages/default.aspx',
	        'scrap_params': {
	                        'carrier_page_1'      : 'li.static:nth-child(3) > a:nth-child(1)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'redrobin': {
	        'search_link'     : 'https://www.redrobin.com/careers/management-jobs.html',
	        'scrap_params': {
	                        'carrier_page_1'      : '.ide20407a9-26b5-48a8-acca-b68ef0c85c19 > a:nth-child(2)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	         
	        'kaiseraluminum': {
	        'search_link'     : 'http://www.kaiseraluminum.com/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > section.main > div > div > div',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'dell': {
	        'search_link'     : 'https://jobs.delltechnologies.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#content > section:nth-child(1) > ul > li:nth-child(1) > div > p:nth-child(3) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'yokesfreshmarkets': {
	        'search_link'     : 'https://www.yokesfreshmarkets.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#block-menu-menu-more > div > ul > li:nth-child(3) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'costargroup': {
	        'search_link'     : 'https://www.costargroup.com/careers/research-opportunities',
	        'scrap_params': {
	                        'carrier_page_1'      : '#aplNowbtn',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'tableau': {
	        'search_link'     : 'https://careers.tableau.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#seeAllCareersBtn > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'safeboats': {
	        'search_link'     : 'http://www.safeboats.com/company/careers.php',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td.ContentZone-TopShadow > div:nth-child(10) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'darigold': {
	        'search_link'     : 'https://www.darigold.com/contact/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div > div > main > section > div > div > div > p:nth-child(4) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'arin': {
	        'search_link'     : 'https://www.arin.net/about/welcome/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#main-con > div > div.right-rail.right-rail-wide > ul:nth-child(2) > li > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },

	        'quest': {
	        'search_link'     : 'https://www.quest.com/company/careers.aspx',
	        'scrap_params': {
	                        'carrier_page_1'      : '#overview > div > div.hero-cta.mt-30.mb-30.cta-container > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'accenture': {
	        'search_link'     : 'https://www.accenture.com/in-en',
	        'scrap_params': {
	                        'carrier_page_1'      : '#primaryLink4_Careers > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > ul:nth-child(3) > li:nth-child(1)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'iridium': {
	        'search_link'     : 'https://www.iridium.com/company-info/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#primaryLink4_Careers > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > ul:nth-child(3) > li:nth-child(1)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'ionaudio': {
	        'search_link'     : 'https://www.ionaudio.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '.ion-footer-menu > ul:nth-child(3) > li:nth-child(3) > span:nth-child(1) > a:nth-child(1)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'jpcycles': {
	        'search_link'     : 'https://www.jpcycles.com/motorcyclesuperstore?utm_source=mssrd',
	        'scrap_params': {
	                        'carrier_page_1'      : '.col_4_5_12 > ul:nth-child(2) > li:nth-child(7) > a:nth-child(1)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'lancair': {
	        'search_link'     : 'https://lancair.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-item-1650 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'gigaom': {
	        'search_link'     : 'https://gigaom.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-item-960019 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'bpa': {
	        'search_link'     : 'https://www.bpa.gov/careers/Pages/default.aspx',
	        'scrap_params': {
	                        'carrier_page_1'      : '#WebPartWPQ1 > ul > li > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'colheli': {
	        'search_link'     : 'https://www.colheli.com/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#page-section-5 > div.page-section-content.vc_row-fluid.mk-grid > div.mk-padding-wrapper.wpb_row > div > div:nth-child(2) > div.wpb_column.vc_column_container.vc_col-sm-8 > div > div > div.vc_btn3-container.col-btn.vc_btn3-center > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'zoomcare': {
	        'search_link'     : 'https://www.zoomcare.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#__layout > div > div.MainFooter > div:nth-child(4) > div > div > div > div > div > div:nth-child(6) > ul > li:nth-child(3) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'dobson': {
	        'search_link'     : 'https://www.dobson.net/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-item-1864 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'columbiasussex': {
	        'search_link'     : 'http://www.columbiasussex.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-item-120 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'deltaprivatejets': {
	        'search_link'     : 'https://www.deltaprivatejets.com/about-delta-private-jets/#careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#careers > div > div > div > div > div > p:nth-child(4) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'siemens': {
	        'search_link'     : 'https://new.siemens.com/global/en/company/jobs.html',
	        'scrap_params': {
	                        'carrier_page_1'      : 'div.references-teaser__button > a:nth-child(1)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'walmart': {
	        'search_link'     : 'https://careers.walmart.com/stores-clubs/walmart-management-jobs',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > main > section.hero.hero--has-cta > div.container.grid.grid--spaced.grid--bottom > div > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'hsn': {
	        'search_link'     : 'https://jobs.hsn.com/jobs-by-category',
	        'scrap_params': {
	                        'carrier_page_1'      : '#content > div.job-category > ul > li',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'scripps': {
	        'search_link'     : 'https://scripps.com/careers/find-a-job/',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div.site > section.basic-content.pb-30 > div > div > div > p:nth-child(3) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'dinsmore': {
	        'search_link'     : 'https://www.dinsmore.com/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-item-26544 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'ge': {
	        'search_link'     : 'https://www.ge.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#wrapper > div.layout.container > div.inner-layout > nav.navbar.navbar-default > div > ul > li:nth-child(3) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'irs': {
	        'search_link'     : 'https://www.jobs.irs.gov/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#block-system-main-menu > ul > li.leaf',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'bostonbeer': {
	        'search_link'     : 'http://www.bostonbeer.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#block-careers-2 > ul > li > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'turnerconstruction': {
	        'search_link'     : 'http://www.turnerconstruction.com/careers/jobs',
	        'scrap_params': {
	                        'carrier_page_1'      : '#content-side > div > strong > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'duke-energy': {
	        'search_link'     : 'https://www.duke-energy.com/our-company/careers',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > main > div:nth-child(2) > section:nth-child(2) > div > footer > p > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'thinkchamplin': {
	        'search_link'     : 'http://www.thinkchamplin.com/sitemap',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > main > div > div.page__main-content > div > div > div > ul > ul:nth-child(2) > li:nth-child(1) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'lyondellbasell': {
	        'search_link'     : 'https://careers.lyondellbasell.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#leftcolumn > div > div:nth-child(2n)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'ashland': {
	        'search_link'     : 'https://www.ashland.com/about/careers/careers-at-ashland',
	        'scrap_params': {
	                        'carrier_page_1'      : '#leftColumn > div > div > p:nth-child(2) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'lpl': {
	        'search_link'     : 'https://careers.lpl.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : 'p.view-all',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'sbarro': {
	        'search_link'     : 'https://sbarro.jobs.net/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#landing-blob-section > tn-content > p:nth-child(15) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'paramount': {
	        'search_link'     : 'https://www.paramount.com/inside-studio/studio/careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#block-system-main > div > article > div > p:nth-child(5) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'newscorp': {
	        'search_link'     : 'https://newscorp.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-item-6669 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'key': {
	        'search_link'     : 'https://www.key.com/about/careers.jsp',
	        'scrap_params': {
	                        'carrier_page_1'      : '#main > article > div.page__content > div:nth-child(2) > div > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'warnerbroscareers': {
	        'search_link'     : 'https://www.warnerbroscareers.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-header-menu > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-1651 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'disneycareers': {
	        'search_link'     : 'https://jobs.disneycareers.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#content > section.featured-jobs > ul > li',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	    
	        'warnermedia': {
	        'search_link'     : 'https://www.att.jobs/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#category-group-warapper > div.job-keyword > ul > li',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	    
	        'verizon': {
	        'search_link'     : 'https://www.verizon.com/about/work',
	        'scrap_params': {
	                        'carrier_page_1'      : '#search_form > div.sj_col.search_jobs__button > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	       'usv': {
	        'search_link'     : 'https://www.usv.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#site-header > div.container > nav > ul.nav.nav-sections.navbar-nav.pull-right.collapse.navbar-toggleable-xs > li:nth-child(5) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	     
	        'pall': {
	        'search_link'     : 'https://www.pall.com/en/careers.html',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > main > div > div > div.career-link.parbase.section > section > div > section.col-33.career-link__container__content__right > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'lillianvernon': {
	        'search_link'     : 'https://www.lillianvernon.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div.page-wrapper > footer > div > div.row > div:nth-child(3) > div > div.block-content > ul > li:nth-child(5) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'tapestry': {
	        'search_link'     : 'https://careers.tapestry.com/viewalljobs/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#categorylist > ul > li',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	    
	        'iac': {
	        'search_link'     : 'https://www.iac.com/careers/overview',
	        'scrap_params': {
	                        'carrier_page_1'      : '#block-menu-block-1 > ul > li.menu-mlid-11662 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'hain': {
	        'search_link'     : 'http://www.hain.com/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#purple-bg-content > div > p:nth-child(3) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'travelers': {
	        'search_link'     : 'https://careers.travelers.com/?_ga=2.1712306.2067520576.1539166870-148981798.1539166870',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-item-4510 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'pentair': {
	        'search_link'     : 'https://www.pentair.com/en/about-pentair/careers.html',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div.sitewide-width-wrapper > main > div.main-content > div:nth-child(1) > section > article > div > div.col-xs-12.col-sm-5 > div > div.cta.parbase.section > div > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'infor': {
	        'search_link'     : 'https://www.infor.com/about',
	        'scrap_params': {
	                        'carrier_page_1'      : 'div.splitBackground-action > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'fico': {
	        'search_link'     : 'https://www.fico.com/en/careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#nav-tab--overview-0 > div > div:nth-child(1) > p > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'startribune': {
	        'search_link'     : 'https://jobs.startribune.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#main > div.band.band--primary.band--primary--third.cf > div > section > div > div > ul > li',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'landolakesinc': {
	        'search_link'     : 'https://www.landolakesinc.com/Careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#wrapper > section > div:nth-child(3) > div > div.small-12.columns.find-your-career > div',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'brsaerospace': {
	        'search_link'     : 'https://brsaerospace.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-item-894 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	    
	        'abdallahcandies': {
	        'search_link'     : 'https://www.abdallahcandies.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#menu-item-38499 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        '3m': {
	        'search_link'     : 'https://www.3m.com/3M/en_US/careers-us/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#pageContent > div.MMM--grids > div > div.component-control.id-Z7_79L2HO02KO83D0Q8I9A4RCI6S1 > div > div > div > div.MMM--featuredBox > div.MMM--tableGrids.MMM--tableGrids_mobile > div.MMM--tableGrids-col.MMM--tableGrids-col_50.MMM--tableGrids-col_border.MMM--tableGrids-col_omega > ul > li:nth-child(2) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'demanddetroit': {
	        'search_link'     : 'https://demanddetroit.com/our-company/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > comp-glue:nth-child(6) > comp-callout > inner-content > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'westbornmarket': {
	        'search_link'     : 'https://www.westbornmarket.com/careers-westborn/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#genesis-content > article > div > div > div.wpb_column.vc_column_container.vc_col-sm-9 > div > div > div > div > p:nth-child(4) > a:nth-child(2)',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'quickenloans': {
	        'search_link'     : 'https://quickenloanscareers.com/?qlsource=nav',
	        'scrap_params': {
	                        'carrier_page_1'      : '#single-blocks > div > div.vc_row.wpb_row.vc_row-fluid.home__hero.vc_custom_1521122111165.wpex-vc_row-has-fill > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(2) > div > div > div.wpb_text_column.wpb_content_element.vc_custom_1545437224404.section-2-copy > div > p:nth-child(2) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'lazboy': {
	        'search_link'     : 'http://jobs.jobvite.com/la-z-boy-review/search?r=&d=&q=',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div > div > div > div.all-job-list > div:nth-child(1) > p > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'jiffymix': {
	        'search_link'     : 'https://site.jiffymix.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#colophon > div.footer_container > div:nth-child(4) > ul > ul > li:nth-child(5) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'gm': {
	        'search_link'     : 'http://www.fabri-kal.com/careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#available-positions > div > header > p > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'spartanmash': {
	        'search_link'     : 'https://careers.spartannash.com/creative/career-retail',
	        'scrap_params': {
	                        'carrier_page_1'      : '#content > section.copy.roles > p > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'cybexintl': {
	        'search_link'     : 'https://www.cybexintl.com/company/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#body-container > div:nth-child(3) > div',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'zoomtel': {
	        'search_link'     : 'http://www.zoomtel.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#footer_main > div > div.footer-main-menu > ul.about-zoom-menu > li:nth-child(5) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'capeair': {
	        'search_link'     : 'https://www.capeair.com/about_us/careers/index.html',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div.container-wrapper.page-content > div > div > table > tbody > tr > td',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'starrett': {
	        'search_link'     : 'http://www.starrett.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#ContentPlaceHolder9_TB3D0EC21005 > div > div > div > ul > li:nth-child(5) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'manulife': {
	        'search_link'     : 'https://jobs.manulife.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#main-content > section.image-callouts.featured-careers > div > div > div',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'fidelity': {
	        'search_link'     : 'https://jobs.fidelity.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#home-page > header > nav > div.nav-wrap.container > div > ul > li:nth-child(6) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'eatonvance': {
	        'search_link'     : 'https://www.eatonvance.com/careers.php',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > main > div > div > center:nth-child(1) > div > div > div > div.col-sm-10 > div > div:nth-child(2) > div > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'cabotcorp': {
	        'search_link'     : 'http://www.cabotcorp.com/company/careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#modules-container > div.promo-module.image.dark-text > div > div > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'neyer': {
	        'search_link'     : 'https://www.neyer.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#work > div > div > div > div > div > div > div > div > div > div > div:nth-child(1) > div > div > div > div > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'galls': {
	        'search_link'     : 'https://www.galls.com/pages/employment',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div.main__wrapper > div > div:nth-child(2) > div > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'qualcomm': {
	        'search_link'     : 'https://www.qualcomm.com/company/careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#qualcomm-careers > div > div.img-or-text__TextColumnContainer-sc-4fwzi7-0.fwQIjs > div.img-or-text__ColumnCtaGroup-sc-4fwzi7-5.QMWfk > div > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'campingworldcareers': {
	        'search_link'     : 'http://www.campingworldcareers.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : '#MainContent > div.container-fluid.page-content.mb-5 > div.row.content-row.pad-bot-60 > div.col-md-12.col-lg-12.col-xl-10 > div > div:nth-child(2) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'yum': {
	        'search_link'     : 'https://www.yum.com/wps/portal/yumbrands/Yumbrands/careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#layoutContainers > div:nth-child(2) > div > div > div > div.stControlBody.stOverflowAuto.wpthemeControlBody > div:nth-child(2) > div > div.container-fluid.hidden-xs > div > nav > section > ul > li:nth-child(5) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'tempursealy': {
	        'search_link'     : 'https://www.tempursealy.com/careers/',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div:nth-child(3) > div:nth-child(3) > div > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'rjcorman': {
	        'search_link'     : 'https://wfa.kronostm.com/index.jsp?locale=en_US&APPLICATIONNAME=RJCormanKTMDReqExt',
	        'scrap_params': {
	                        'carrier_page_1'      : '#Div7',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'paducahbank': {
	        'search_link'     : 'https://www.paducahbank.com/Learn/Company-Information/Careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#mainContent > div.categories > div > div:nth-child(1) > div.col.col-xs-12.col-sm-6.col-md-5.col-md-push-1.col-lg-4.col-lg-push-2 > div > p:nth-child(2) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        'lexmark': {
	        'search_link'     : 'https://www.lexmark.com/en_us/careers.html',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > div.slide-in-panel__page-container > div.par.parsys > div.row.container.section.l-pad > div.col-3-4 > div > div > div.col-1-3 > div > div:nth-child(1) > div > h3 > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'heavenhill': {
	        'search_link'     : 'http://www.heavenhill.com/',
	        'scrap_params': {
	                        'carrier_page_1'      : 'body > header > div > div > div > ul > li:nth-child(6) > ul > li:nth-child(2) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	        
	        'fazolis': {
	        'search_link'     : 'https://www.fazolis.jobs/index.cfm',
	        'scrap_params': {
	                        'carrier_page_1'      : '#navigationDiv > div:nth-child(6) > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
            'moback': {
	        'search_link'     : 'https://www.moback.com/careers',
	        'scrap_params': {
	                        'carrier_page_1'      : '#root > div > div > div > div > section:nth-child(4) > p.more-link > a',
	                        'title'               :  None,
	                        'carrier_page_2'      :  '#menu-item-266'
	                        
	                        }
	                    },
	    }
	        

	

	#function for getting the carrier page information
	def JobPortalData(self, company_list):

	    class AppURLopener(urllib.request.FancyURLopener):
	        version = "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"

	    companys_list  = []
	    time.sleep(3)
	    #print(company_list)

	    Jobportal_metadata  = self.Jobportal_initials[company_list]
	    
	    Jobportal_link      = Jobportal_metadata['search_link']
	    scrap_params        = Jobportal_metadata['scrap_params']
	    carrier_page_1      = scrap_params['carrier_page_1']
	    title_selector      = scrap_params['title']
	    carrier_page_2      = scrap_params['carrier_page_2']
	    opener = AppURLopener()
	    page = opener.open(Jobportal_link)
	    
	    #page           = requests.get(jobportal_url)  
	    time.sleep(2)

	    page_soup      = soup(page, 'html.parser')

	    containers     = page_soup.select(carrier_page_1)
	    #print(containers) 
	    from pprint import pprint

	    
	    
	    for container in containers:
	        #Collecting the Company list by state wise
	        try:
	            link = container.a['href']
	            #print(link)
	            #print("ss")
	            
	            if  company_list=='accenture':
	              link=self.accenture+link

	            elif  company_list=='hsn':
	              link=self.hsn+link

	            elif  company_list=='irs':
	              link=self.irs+link

	            elif  company_list=='lyondellbasell':
	              link=self.lyondell+link

	            elif  company_list=='lpl':
	              link=self.lpl+link
	            
	            elif  company_list=='disneycareers':
	              link=self.disney+link
	            
	            elif  company_list=='warnermedia':
	              link=self.warnermedia+link
	            
	            elif  company_list=='tapestry':
	              link=self.tapestry+link
	              
	            elif  company_list=='startribune':
	              link=self.startribune+link
	            
	            elif  company_list=='manulife':
	              link=self.manulife+link
	              
	            else :
	                print( " ")
	            #print(link)
	        except:
	           
	            link=container['href']
	            #print(link)
	            
	            if  company_list=='ebags':
	              link=self.ebags+link
	 
	            elif  company_list=='lovesac':
	              link= self.lovesac+link

	            elif  company_list=='rhone':
	              link= self.rhone+link

	            elif  company_list=='altria':
	              link= self.altria_1+link+altria

	            elif company_list=='dell':
	                link=self.dell+link

	            elif  company_list=='tableau':
	              link= self.tableau+link

	            elif  company_list=='arin':
	              link= self.arin+link

	            elif  company_list=='jpcycles':
	              link= self.jpcycles+link

	            elif  company_list=='gigaom':
	              link= self.gigaom+link
	 
	            elif  company_list=='zoomcare':
	              link= self.zoomcare+link

	            elif  company_list=='walmart':
	              link= self.walmart+link

	            elif  company_list=='thinkchamplin.':
	              link= self.thinkchamp+link
	              
	            elif  company_list=='sbarro':
	              link= self.sbarro+link 
	              
	            elif  company_list=='newscorp':
	              link= self.newscrop+link 
	              
	            elif  company_list=='key':
	              link= self.key+link 
	            
	            elif  company_list=='verizon':
	              link= self.verizon+link 
	            
	            elif  company_list=='iac':
	              link= self.iac+link 
	              
	            elif  company_list=='masco':
	              link= self.masco+link 
	              
	            elif  company_list=='lazboy':
	              link= self.lazboy+link 
	              
	            elif  company_list=='jiffymix':
	              link= self.jiffymix+link 
	              
	            elif  company_list=='spartanmash':
	              ve=link.replace('../','/')  
	              link=self.spartanmash+ve  
	              
	            elif  company_list=='starrett':
	              link= self.starrett+link  
	            
	            elif  company_list=='fidelity':
	              link= self.fidelity+link 
	              
	            elif  company_list=='yum':
	              link= self.yum+link
	              
	            elif  company_list=='rjcorman':
	              link= self.rjcorman+link
	             
	            elif  company_list=='lexmark':
	              link= self.lexmark+link
	              
	            elif  company_list=='heavenhill':
	              link= self.heavenhill+link
	            elif  company_list=='moback':
	              link= self.moback+link
	              
	            else :
	                print( " ") 
	        try:
	            if title_selector is not None:
	                title      = container.select_one(title_selector)
	                title_text = title.text.strip('\n').strip('\t')
	            else :
	                title_text = container.text.strip('\n').strip('\t')
	            

	        except Exception as e:
	            print("Something went wrong while fetching  data" + \
	                   " from  " + company_list )
	        else :
	            companys_list.append(link)
	    return companys_list






#company_names = []

args={}

company_names=[]
def create_view(request):

	global company_names


	if request.method == "POST":		
		company_names = request.POST['input']

	#return company_names

	return render( request,"inde.html") 

#print()
"""


def create_view(request):
	global COMPANY_LIST, args
	#print(request.GET)
	#print(request.POST)
	#company_namess=[]

	if request.method == "GET":
		args = {}

	if request.method == "POST":		
		company_names = request.POST['input']
	#	company_name.append(company_names)
	#	print(company_name)
		if company_names:
			company_class = HomePageView()
			company_list= company_names.split(",")
			for company_list_name in company_list:
				Job_Protal_data = company_class.JobPortalData(company_list_name)
			
			COMPANY_LIST[company_list_name] = Job_Protal_data[0]
			#print(COMPANY_LIST)

			args = {"Company":COMPANY_LIST}
		else:
			args = {}


	return render( request,"index.html",  args) 
print("printing company names")	
print(args)
"""
def create_api(request):
	
	api_list= {"company_name":company_names}


	#COMPANY_LIST[company_list_name] = api_list[0]
	#print(type(api_list))


	#args_api = {"Companys":api_list}
		

	return render(request,"api.html", {"args_api":api_list})