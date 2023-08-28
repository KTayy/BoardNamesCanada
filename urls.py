import CleanerFunctions as clnr


URLS = {
        
        
    "OTPP": 
        {
        "location": 
            [
            "https://www.otpp.com/en-ca/about-us/our-leadership/",
            "div",
            {"class": "op-bio-card__title my-2"}
            ],
    },
        

    "OPB": 
        {
        "location": 
            [
            "https://www.opb.ca/about-opb/board-of-directors",
            "div",
            {"class": "opb-board-content"}
            ],
        "function": clnr.opb_clean_soup
    },
        

    "IMCO": 
        {
        "location": 
            [
            "https://www.imcoinvest.com/board-of-directors.html",
            "h3",
            {"class": "a-heading__h3 a-heading__margin-small has-link"}
            ],
        "function" : clnr.imco_clean_soup
    },
        

    "BMO": 
        {
        "location": 
            [
            "https://www.bmo.com/home/about/banking/corporate-governance/board-of-directors",
            "h2",
            {"class": "bio-name"}
            ],
        "function" : clnr.bmo_clean_soup
    },
        

    "CIBC": 
        {
        "location": 
            [
            "https://www.cibc.com/en/about-cibc/corporate-governance/board-of-directors/board-members.html",
            'span',
            {"class": "subhead-medium-light"}
            ]
    },

                

                
        "AIMCO" : 
            {
            "location" :
                [
                    "https://www.aimco.ca/who-we-are/governance",
                    "p", 
                    {"class": "person-name"}
                ],
            "function" : clnr.aimco_clean_soup
            },
        
             
        "Manulife" :
            {
            "location" : 
                [
                    "https://www.manulife.com/en/about/corporate-governance/board-of-directors.html",
                    "div",
                    {"class" : "cmp-titletext"}
                ],
            "function" : clnr.manulife_clean_soup
            },
                
                
        "NBC" : {
            "location":
                        
                [
                    "https://www.nbc.ca/about-us/news-media/press-release/2023/20230421-nbc-election-directors.html",
                    "div", 
                    {"class": "text table_style aem-GridColumn aem-GridColumn--default--12"}
                ],
            "function" : clnr.nbc_clean_soup
            },
            
    
        "RBC" : 
            {
            "location":
                [
                    "https://www.rbc.com/our-company/governance/index.html",
                    "h2", 
                    {"class": "h5 eh"}
                ],
            "function": clnr.rbc_clean_soup
            }, 
            
            
        "SCOTIABANK" : 
            {
            "location":
                [
                    "https://www.scotiabank.com/ca/en/about/our-company/board-of-directors.html",
                    "div", 
                    {"class": "cmp cmp-text"}
                ],
            "function" : clnr.scotiabank_clean_soup    
            },
        
        
        "TD" :
            {
            "location" :
                [
                    "https://www.td.com/ca/en/about-td/corporate-profile/board-members",
                    "div", 
                    {"class": "cmp cmp-text"}
                ],
            "function" : clnr.td_clean_soup
            },

                
        "AIG" :
            {
            "location":
                [
                    "https://www.aig.com/home/about/leadership-and-governance",
                    "div", 
                    {"class": 'container responsivegrid tabbed-cards flexbox-container addtoppadding10 aem-GridColumn aem-GridColumn--default--12'},
                    "div",
                    {"class": 'cmp-teaser__description' }
                ],
            "function" : clnr.aig_clean_soup
            },
            
            
        "BDC" : 
            {
            "location" :
                [
                    "https://www.bdc.ca/en/about/corporate-governance/board-of-directors",
                    "h4"
                ],
            "function" : clnr.bdc_clean_soup
            },
            
            
        "CDIC" : {
            "location" :
        [
            "https://www.cdic.ca/about-us/organizational-structure/our-board-of-directors/cdic-board-of-directors-biographies/",
            "p", 
            {"class": "h4"}
        ],  
            "function" : clnr.cdic_clean_soup
            },
            
                        
        "CIB" : {
            "location" :
        [
            "https://cib-bic.ca/en/about-us/governance/",
            "div", 
            {"class": "person-title  font-semibold text-red-100 hover:underline text-xl-22"}
        ], 
            "function" : clnr.cib_clean_soup
            },
            
                        
        "CMHC" : {
            "location" :
            [
                "https://www.cmhc-schl.gc.ca/about-us/management-and-governance/board-of-directors-and-its-committees",
                "div", 
                {"class": "imageTilesContent"}
            ],
            "function" : clnr.cmhc_clean_soup
            },
                        
        "CDPQ" : {
            "location" :
            [
                "https://www.cdpq.com/en/about-us/governance/board-directors",
                "h3", 
                {"class": "title-sm-bio mb-1 pb__fullname"}
            ],
            "function": clnr.cdpq_clean_soup
            },
                        
        "CPPIB" : {
             "location" :
        [
            "https://www.cppinvestments.com/about-us/governance/board-of-directors/",
            "h2", 
            {"class": "card-header-text"}
        ],
            "function" : clnr.cppib_clean_soup
            },
            
            
        "DEFENITY" :{
            "location" :#static
        [
            "https://www.definityfinancial.com/English/investors/governance/board-of-directors/default.aspx",
            "h2", 
            {"class": "person_name person_name--president h3 no-top--desktop no-top--tablet"}
        ],
        "function" : clnr.defenity_clean_soup
        },
        
                        
        "DESJARDINS" :{
            "location":#static
        [
            "https://www.desjardins.com/ca/about-us/desjardins/governance-democracy/board-directors/index.jsp",
            "H3", 
            {"class": "titre"}
        ],
        "function" : clnr.desjardins_clean_soup
        },
                        
        
        "EQUITABLE BANK" : {
            "location": 
        [
            "https://eqbank.investorroom.com/board-directors",
            "h2", 
            {"class": "wd_title"}
        ], 
        "function": clnr.equitable_clean_soup
        },
        
                        
        "EDC" : #static
        {"location":
        [
            "https://www.edc.ca/en/about-us/corporate/management-governance.html",
            "span", 
            {"class": "name"}
        ],
        "function":clnr.edc_clean_soup
        },
            
            
        "FAIRFAX" : {"error_message" : "FAIRFAX has no board member page"}, # not available!!!!!!!!
        
                        
        "HOME CAPITAL" : 
            {"location":
        [
            "https://www.hometrust.ca/about/our-story/leadership/",
            "div", 
            {"class": "service_title"}
        ], 
        "function" : clnr.home_clean_soup
        },
                
                        
        "IESO" : 
            {"location":
        [
            "https://www.ieso.ca/en/Corporate-IESO/Leadership/Board-of-Directors",
            "div", 
            {"class": "sidebarBlock richText "}
        ],
            "function":clnr.ieso_clean_soup
            },
                 
                
        "LAURENTIAN" : #static
        {"location" :
        [
            "https://www.laurentianbank.ca/en/about-us/our-company/board-of-directors",
            "h3",
            {"class": "font-bold leading-[1.1em] text-3xl text-brand-web-lbc-blue"}
        ],
        "function" : clnr.laurentian_clean_soup},
                        
            
        "MERIDIAN" : #static
        {"location" :
        [
            "https://www.meridiancu.ca/about-meridian/corporate/governance/board-of-directors",
            "h2", 
            {"class": "small-margin"}
        ],
        "function" : clnr.meridian_clean_soup},
                     
            
            
        "MUNICH RE" : #static
        {"location" : 
        [
            "https://www.munichre.com/en/company/about-munich-re/board-of-management/members.html",
            "h2", 
            {"class": "cmp-title__text"}
        ],
        "function": clnr.munich_clean_soup
         },
         
                        
        "OMERS" : #static
        {"location" : 
        [
            "https://www.omers.com/board-of-directors",
            "span", 
            {"class": "bold"}
        ],
        "function": clnr.omers_clean_soup
        },

                
        "OPTRUST" : #static
        {"location" :
        [
            "https://www.optrust.com/aboutoptrust/Board-of-Trustees.asp",
            "h5"
        ],
        "function" : clnr.optrust_clean_soup
            },
        
        
                        
        "PAYMENTS CANADA" : #static
        {"location":
        [
            "https://payments.ca/about/governance-risk/board-directors",
            "h3"
        ],
        "function" :clnr.payments_clean_soup
        },
            
        "PC BANK" :  {"error_message": "PC Bank has no board member page"},
                        
        "CANADA LIFE" : #static
        {"location":
        [
            "https://www.canadalife.com/about-us/governance/board-of-directors.html",
            "span", 
            {"class": "n-card__title-link has-no-margins-around n:my-0"}
        ],
        "function" :clnr.canadalife_clean_soup
        },
            
            
                        
        "IGM FINANCIAL" : #static
        
        {"location" :
        [
            "https://www.igmfinancial.com/en/governance",
            "b" 
            #{"class": "location2"}
        ],
        "function" : clnr.igm_clean_soup},
            
                        
        "MACKENZIE INVESTMENTS" : #static
        {"location" :
        [
            "https://www.mackenzieinvestments.com/en/about-us/leadership-team",
            "p", 
            {"class": "text-primary type-medium margin-bottom-none padding-bottom-none  padding-top-sm"}
        ],
        "function" : clnr.mackenzie_clean_soup},
            
            
                        
        "PSP INVESTMENTS" : #static
        {"location" :
        
        [
            "https://www.investpsp.com/en/psp/board/",
            "div", 
            {"class": "tp-people-name"}
        ],
        "function" : clnr.psp_clean_soup
        
        },
                        
        "QUESTRADE" : { "error_message" : "Questrade is not a public company" },
        
                        
        "SAGICOR" : #static
        {"location":
        [
            "https://www.sagicor.com/en/about-sagicor/board-of-directors",
            "h4", 
            #{"location2": "location3"}
        ],
        "function": clnr.sagicor_clean_soup
        },
        
                        
        "SUN LIFE" : {
        "location" : 
        [
            "https://www.sunlife.com/en/about-us/leadership/board-of-directors/",
            "div", 
            {"class": "col-sm-6"}
        ],
        "function" : clnr.sunlife_clean_soup
        },
        
            
        "VANCITY" : #static
        {
            "location":
        [
            "https://www.vancity.com/AboutVancity/GovernanceAndLeadership/BoardofDirectors/CurrentBoard/",
            "div", 
            {"class": "mainContent"}
        ],
            "function" : clnr.vancity_clean_soup
            },
            
        "UPP": 
            {
            "location": 
                [
                "https://myupp.ca/about-us/governance/#:~:text=The%20Board%20includes%20six%20Trustees,independent%2C%20jointly%2Dselected%20Chair.",
                "elementor-heading-title elementor-size-default"
                ],
            "function": clnr.upp_clean_soup
        }
        
    }

