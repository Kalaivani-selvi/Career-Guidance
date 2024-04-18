import pandas as pd
import random

# Define the list of UG Courses and their respective specializations
ug_courses = {
    "BA": ["English Literature", "History", "Economics", "Psychology"],
    "BSc": ["Physics", "Chemistry", "Mathematics", "Biology"],
    "BCom": ["Accounting", "Finance", "Marketing", "Management"],
    "BE or BTech": ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering"],
    "BFA": ["Fine Arts", "Sculpture", "Painting", "Graphic Design"],
    "BBA": ["Business Administration", "Entrepreneurship", "International Business", "Human Resource Management"],
    "BArch": ["Architecture", "Urban Planning", "Interior Design", "Landscape Architecture"],
    "BCA": ["Computer Applications", "Information Technology", "Software Engineering", "Web Development"],
    "BEd": ["Elementary Education", "Secondary Education", "Special Education", "Early Childhood Education"],
    "BSA": ["Astronomy", "Astrophysics", "Space Engineering", "Space Technology"]
}

# Define job roles according to UG courses
job_roles = {
   "BA": {
    "Content Writer": {
        "Summary": "Writes and edits content for various platforms and purposes.",
        "Responsibilities": ["Researching topics and generating ideas for content",
                             "Writing and editing content for websites, blogs, or other publications",
                             "Collaborating with team members to brainstorm and develop content strategies",
                             "Proofreading and ensuring content is accurate and engaging"],
        "Qualifications": ["Excellent writing and editing skills",
                          "Strong research and analytical abilities",
                          "Creativity and attention to detail",
                          "Ability to meet deadlines and work independently or in a team"],
        "Industry Type": "Media, Marketing, Publishing"
    },
    "Social Media Manager": {
        "Summary": "Manages social media presence and engagement for individuals or organizations.",
        "Responsibilities": ["Developing social media strategies to increase brand awareness and engagement",
                             "Creating and curating content for social media platforms",
                             "Monitoring social media channels for trends and opportunities",
                             "Analyzing social media metrics and optimizing strategies accordingly"],
        "Qualifications": ["Strong understanding of social media platforms and trends",
                          "Excellent communication and interpersonal skills",
                          "Experience with social media management tools",
                          "Ability to think creatively and strategically"],
        "Industry Type": "Marketing, Advertising, Public Relations"
    },
    "Marketing Coordinator": {
        "Summary": "Coordinates marketing activities and campaigns.",
        "Responsibilities": ["Assisting in the development and implementation of marketing plans",
                             "Coordinating marketing campaigns across various channels",
                             "Conducting market research and analyzing consumer behavior",
                             "Assisting with the creation of marketing materials and collateral"],
        "Qualifications": ["Strong organizational and project management skills",
                          "Excellent communication and interpersonal abilities",
                          "Understanding of marketing principles and techniques",
                          "Ability to work effectively in a fast-paced environment"],
        "Industry Type": "Marketing, Advertising, Sales"
    },
    "Human Resources Assistant": {
        "Summary": "Assists in various HR functions such as recruitment, onboarding, and employee relations.",
        "Responsibilities": ["Assisting with recruitment efforts, including posting job openings and scheduling interviews",
                             "Coordinating employee onboarding and orientation programs",
                             "Maintaining employee records and databases",
                             "Assisting with employee relations issues and conflict resolution"],
        "Qualifications": ["Strong organizational and administrative skills",
                          "Ability to maintain confidentiality and handle sensitive information",
                          "Knowledge of HR policies and procedures",
                          "Excellent interpersonal and communication abilities"],
        "Industry Type": "Human Resources, Recruitment"
    },
    "Public Relations Specialist": {
        "Summary": "Manages public relations and communications for individuals or organizations.",
        "Responsibilities": ["Developing and implementing PR strategies to enhance brand visibility",
                             "Writing press releases, articles, and other PR materials",
                             "Building and maintaining relationships with media contacts",
                             "Monitoring media coverage and preparing reports for clients or management"],
        "Qualifications": ["Excellent written and verbal communication skills",
                          "Strong interpersonal and networking abilities",
                          "Ability to work under pressure and meet tight deadlines",
                          "Understanding of media relations and PR best practices"],
        "Industry Type": "Public Relations, Communications"
    },
    "Event Planner": {
        "Summary": "Plans and organizes events such as conferences, weddings, and corporate gatherings.",
        "Responsibilities": ["Meeting with clients to discuss event requirements and budgets",
                             "Researching and booking venues, suppliers, and entertainment",
                             "Coordinating logistics such as catering, transportation, and accommodations",
                             "Overseeing event setup, execution, and breakdown"],
        "Qualifications": ["Strong organizational and multitasking skills",
                          "Attention to detail and ability to problem-solve on the fly",
                          "Excellent communication and negotiation abilities",
                          "Experience with event planning software and tools"],
        "Industry Type": "Event Management, Hospitality"
    },
    "Copywriter": {
        "Summary": "Writes copy for advertisements, websites, and promotional materials.",
        "Responsibilities": ["Researching and understanding target audiences and market trends",
                             "Writing clear, concise, and compelling copy for various mediums",
                             "Collaborating with designers and marketers to develop creative concepts",
                             "Proofreading and editing copy to ensure accuracy and consistency"],
        "Qualifications": ["Strong writing and editing skills",
                          "Creativity and ability to generate innovative ideas",
                          "Understanding of branding and marketing principles",
                          "Ability to work collaboratively and meet deadlines"],
        "Industry Type": "Advertising, Marketing, Publishing"
    },
    "Customer Service Representative": {
        "Summary": "Handles customer inquiries, complaints, and support requests.",
        "Responsibilities": ["Responding to customer inquiries via phone, email, or chat",
                             "Resolving customer complaints and issues in a timely and professional manner",
                             "Providing product information and assistance to customers",
                             "Documenting customer interactions and maintaining records"],
        "Qualifications": ["Excellent communication and interpersonal skills",
                          "Patience and empathy when dealing with customers",
                          "Ability to remain calm and professional under pressure",
                          "Basic computer and problem-solving skills"],
        "Industry Type": "Customer Service, Retail, E-commerce"
    },
    "Journalist": {
        "Summary": "Researches, writes, and reports news stories for various media outlets.",
        "Responsibilities": ["Conducting research and interviews to gather information for stories",
                             "Writing and editing news articles, features, and investigative reports",
                             "Adhering to journalistic ethics and standards",
                             "Meeting tight deadlines and working under pressure"],
        "Qualifications": ["Strong writing and storytelling abilities",
                          "Excellent research and investigative skills",
                          "Ability to work independently and collaboratively",
                          "Knowledge of media law and ethics"],
        "Industry Type": "Media, Journalism"
    },
    "Fundraiser": {
        "Summary": "Organizes and executes fundraising campaigns and events.",
        "Responsibilities": ["Developing fundraising strategies and campaigns",
                             "Identifying and cultivating potential donors and sponsors",
                             "Organizing and promoting fundraising events and activities",
                             "Tracking and reporting on fundraising metrics and goals"],
        "Qualifications": ["Strong communication and interpersonal skills",
                          "Ability to build and maintain relationships with donors",
                          "Experience in event planning and project management",
                          "Understanding of fundraising principles and techniques"],
        "Industry Type": "Nonprofit, Fundraising"
    }
},    
      "BSc": { 
    "Research Scientist": {
        "Summary": "Conducts scientific research in various fields.",
        "Responsibilities": ["Designing and conducting experiments to answer specific research questions",
                             "Collecting and analyzing data using scientific methods and techniques",
                             "Writing research papers, reports, and grant proposals",
                             "Collaborating with other scientists and researchers on projects"],
        "Qualifications": ["Strong scientific knowledge and research skills",
                          "Ability to design and execute experiments independently",
                          "Excellent analytical and critical thinking abilities",
                          "Effective communication and teamwork skills"],
        "Industry Type": "Research, Academia, Pharmaceuticals"
    },
    "Lab Technician": {
        "Summary": "Assists in laboratory experiments and procedures.",
        "Responsibilities": ["Preparing and setting up laboratory equipment and instruments",
                             "Collecting and processing samples for analysis",
                             "Conducting experiments under the supervision of scientists or researchers",
                             "Maintaining laboratory cleanliness and safety standards"],
        "Qualifications": ["Knowledge of laboratory techniques and procedures",
                          "Attention to detail and ability to follow protocols",
                          "Good organizational and time management skills",
                          "Ability to work effectively in a team environment"],
        "Industry Type": "Research, Healthcare, Pharmaceuticals"
    },
    "Data Analyst": {
        "Summary": "Analyzes data to extract insights and inform decision-making.",
        "Responsibilities": ["Cleaning, transforming, and validating data for analysis",
                             "Applying statistical and machine learning techniques to analyze data",
                             "Creating visualizations and reports to present findings",
                             "Interpreting data and providing actionable insights to stakeholders"],
        "Qualifications": ["Strong analytical and problem-solving skills",
                          "Proficiency in statistical analysis and data visualization tools",
                          "Experience with database querying and programming languages",
                          "Ability to communicate complex findings to non-technical audiences"],
        "Industry Type": "Data Science, Analytics, Consulting"
    },
    "Environmental Scientist": {
        "Summary": "Studies the environment and its interactions with living organisms.",
        "Responsibilities": ["Collecting and analyzing environmental samples",
                             "Assessing environmental impacts and risks",
                             "Developing and implementing plans to mitigate environmental problems",
                             "Communicating findings to policymakers, businesses, and the public"],
        "Qualifications": ["Knowledge of environmental science principles and regulations",
                          "Fieldwork experience and proficiency in data collection methods",
                          "Critical thinking and problem-solving abilities",
                          "Effective written and oral communication skills"],
        "Industry Type": "Environmental Consulting, Government, Nonprofit"
    },
    "Pharmaceutical Sales Representative": {
        "Summary": "Sells pharmaceutical products to healthcare providers.",
        "Responsibilities": ["Promoting pharmaceutical products to healthcare professionals",
                             "Building and maintaining relationships with customers",
                             "Providing product information and education to healthcare providers",
                             "Achieving sales targets and objectives"],
        "Qualifications": ["Strong sales and negotiation skills",
                          "Knowledge of pharmaceutical products and industry regulations",
                          "Excellent communication and interpersonal abilities",
                          "Ability to work independently and manage time effectively"],
        "Industry Type": "Pharmaceuticals, Healthcare"
    },
    "Biomedical Engineer": {
        "Summary": "Designs and develops medical devices and equipment.",
        "Responsibilities": ["Conducting research to develop new medical devices and technologies",
                             "Designing and prototyping medical devices and equipment",
                             "Testing and evaluating prototypes for safety and efficacy",
                             "Collaborating with healthcare professionals to identify needs and requirements"],
        "Qualifications": ["Strong engineering background with knowledge of biology and physiology",
                          "Experience with CAD software and medical device regulations",
                          "Problem-solving and critical thinking skills",
                          "Ability to work in multidisciplinary teams"],
        "Industry Type": "Biomedical Engineering, Medical Devices"
    },
    "Statistician": {
        "Summary": "Applies statistical methods to analyze data and solve problems.",
        "Responsibilities": ["Designing experiments and surveys to collect data",
                             "Analyzing data using statistical software and techniques",
                             "Interpreting and communicating results to stakeholders",
                             "Providing statistical expertise and support to research projects"],
        "Qualifications": ["Strong mathematical and statistical skills",
                          "Proficiency in statistical software such as R or SAS",
                          "Critical thinking and problem-solving abilities",
                          "Excellent communication and collaboration skills"],
        "Industry Type": "Research, Consulting, Government"
    },
    "Quality Control Analyst": {
        "Summary": "Ensures products meet quality standards through testing and analysis.",
        "Responsibilities": ["Performing quality control tests and inspections on products",
                             "Recording and analyzing test results",
                             "Identifying and addressing quality issues and non-conformances",
                             "Developing and implementing quality control procedures"],
        "Qualifications": ["Knowledge of quality control principles and techniques",
                          "Attention to detail and accuracy in testing and analysis",
                          "Ability to interpret technical specifications and requirements",
                          "Strong problem-solving and decision-making skills"],
        "Industry Type": "Manufacturing, Pharmaceuticals, Food and Beverage"
    },
    "Forensic Scientist": {
        "Summary": "Applies scientific principles to solve crimes and analyze evidence.",
        "Responsibilities": ["Collecting, analyzing, and interpreting physical evidence from crime scenes",
                             "Using laboratory techniques and equipment to analyze evidence",
                             "Preparing reports and presenting findings in court",
                             "Collaborating with law enforcement agencies and legal professionals"],
        "Qualifications": ["Strong scientific background with knowledge of forensic science principles",
                          "Experience with forensic techniques and evidence handling",
                          "Attention to detail and ability to maintain chain of custody",
                          "Effective written and verbal communication skills"],
        "Industry Type": "Law Enforcement, Forensic Science"
    },
    "Epidemiologist": {
        "Summary": "Studies patterns and causes of diseases in populations.",
        "Responsibilities": ["Collecting and analyzing health data to identify trends and patterns",
                             "Investigating disease outbreaks and identifying risk factors",
                             "Developing and implementing strategies for disease prevention and control",
                             "Communicating findings to public health officials and policymakers"],
        "Qualifications": ["Strong analytical and research skills",
                          "Knowledge of epidemiological methods and study design",
                          "Understanding of public health principles and practices",
                          "Ability to work collaboratively in multidisciplinary teams"],
        "Industry Type": "Public Health, Epidemiology"
    }
   },
"BCom": {
        "Accountant": {
            "Summary": "Manages financial records and prepares financial statements.",
            "Responsibilities": ["Recording financial transactions and preparing financial reports",
                                 "Analyzing financial data and advising on financial decisions",
                                 "Ensuring compliance with accounting principles and regulations",
                                 "Preparing tax returns and assisting with audits"],
            "Qualifications": ["Bachelor's degree in accounting or related field",
                              "Certification as a Chartered Accountant or CPA (preferred)",
                              "Proficiency in accounting software and Microsoft Excel",
                              "Strong analytical and problem-solving skills"],
            "Industry Type": "Finance, Accounting, Consulting"
        },
        "Financial Analyst": {
            "Summary": "Analyzes financial data and provides insights to support decision-making and planning.",
            "Responsibilities": ["Analyzing financial statements and performance metrics",
                                 "Forecasting financial trends and preparing financial models",
                                 "Conducting industry research and providing investment recommendations",
                                 "Preparing reports and presentations for stakeholders"],
            "Qualifications": ["Bachelor's degree in finance, economics, or related field",
                              "Strong quantitative and analytical skills",
                              "Proficiency in financial modeling and data analysis tools",
                              "Effective communication and presentation abilities"],
            "Industry Type": "Finance, Investment, Consulting"
        },
        "Sales Executive": {
            "Summary": "Sells products or services to customers.",
            "Responsibilities": ["Identifying and contacting potential customers",
                                 "Presenting product features and benefits to customers",
                                 "Negotiating prices and terms of sale",
                                 "Building and maintaining relationships with clients"],
            "Qualifications": ["Bachelor's degree in business or related field",
                              "Proven sales experience and track record of achieving targets",
                              "Excellent communication and interpersonal skills",
                              "Ability to work independently and as part of a team"],
            "Industry Type": "Sales, Marketing, Retail"
        },
        "Business Consultant": {
            "Summary": "Provides expert advice to businesses to improve performance and solve problems.",
            "Responsibilities": ["Assessing business processes and identifying areas for improvement",
                                 "Developing and implementing strategic plans and initiatives",
                                 "Analyzing data and providing recommendations for business growth",
                                 "Training and coaching employees on best practices"],
            "Qualifications": ["Bachelor's degree in business, management, or related field",
                              "Proven experience in consulting or relevant industry",
                              "Strong analytical and problem-solving skills",
                              "Excellent communication and presentation abilities"],
            "Industry Type": "Consulting, Management, Business Services"
        },
        "Investment Analyst": {
            "Summary": "Analyzes investment opportunities and makes recommendations.",
            "Responsibilities": ["Conducting financial analysis and research on investment options",
                                 "Evaluating risks and returns of potential investments",
                                 "Preparing investment reports and presentations",
                                 "Monitoring market trends and providing investment advice"],
            "Qualifications": ["Bachelor's degree in finance, economics, or related field",
                              "Certification such as CFA or Chartered Financial Analyst (preferred)",
                              "Strong analytical and research skills",
                              "Knowledge of financial markets and investment strategies"],
            "Industry Type": "Finance, Investment, Wealth Management"
        },
        "Risk Analyst": {
            "Summary": "Assesses and manages risks faced by individuals or organizations.",
            "Responsibilities": ["Identifying potential risks and vulnerabilities",
                                 "Analyzing data to assess the likelihood and impact of risks",
                                 "Developing risk management strategies and policies",
                                 "Monitoring and reporting on risk exposures"],
            "Qualifications": ["Bachelor's degree in risk management, finance, or related field",
                              "Strong analytical and problem-solving skills",
                              "Knowledge of risk assessment methodologies and regulations",
                              "Attention to detail and ability to communicate complex concepts"],
            "Industry Type": "Risk Management, Insurance, Banking"
        },
        "Tax Consultant": {
            "Summary": "Provides guidance on tax-related matters.",
            "Responsibilities": ["Advising clients on tax planning and compliance",
                                 "Preparing and reviewing tax returns and documents",
                                 "Resolving tax issues and disputes with tax authorities",
                                 "Staying informed about changes in tax laws and regulations"],
            "Qualifications": ["Bachelor's degree in accounting, finance, or related field",
                              "Certification as a tax professional (e.g., CPA, Enrolled Agent)",
                              "Knowledge of tax laws and regulations",
                              "Strong analytical and problem-solving skills"],
            "Industry Type": "Taxation, Accounting, Consulting"
        },
        "Auditor": {
            "Summary": "Examines financial records to ensure accuracy and compliance with regulations.",
            "Responsibilities": ["Reviewing financial statements and accounting records",
                                 "Conducting audits to assess compliance with laws and regulations",
                                 "Identifying areas for improvement in internal controls",
                                 "Preparing audit reports and recommendations for management"],
            "Qualifications": ["Bachelor's degree in accounting, finance, or related field",
                              "Certification as a Certified Internal Auditor (CIA) or Certified Public Accountant (CPA)",
                              "Experience in auditing or accounting",
                              "Attention to detail and strong analytical skills"],
            "Industry Type": "Accounting, Auditing, Consulting"
        },
        "Retail Manager": {
            "Summary": "Manages operations and staff in retail establishments.",
            "Responsibilities": ["Overseeing day-to-day operations of the retail store",
                                 "Managing inventory and ensuring stock levels are adequate",
                                 "Recruiting, training, and supervising retail staff",
                                 "Providing excellent customer service and resolving complaints"],
            "Qualifications": ["Bachelor's degree in business, retail management, or related field",
                              "Proven experience in retail management or sales",
                              "Leadership and team management skills",
                              "Knowledge of retail industry trends and best practices"],
            "Industry Type": "Retail, Sales, Customer Service"
        },
        "E-commerce Manager": {
            "Summary": "Manages online sales platforms and digital marketing efforts.",
            "Responsibilities": ["Developing and implementing e-commerce strategies to drive sales",
                                 "Managing online product listings, pricing, and promotions",
                                 "Optimizing website usability and user experience",
                                 "Analyzing e-commerce performance metrics and making data-driven decisions"],
            "Qualifications": ["Bachelor's degree in marketing, business, or related field",
                              "Experience in e-commerce management or digital marketing",
                              "Knowledge of e-commerce platforms and technologies",
                              "Strong analytical and problem-solving skills"],
            "Industry Type": "E-commerce, Digital Marketing, Retail"
        }
},
    "BE or BTech": {
        "Software Engineer": {
            "Summary": "Designs, develops, and maintains software applications.",
            "Responsibilities": ["Analyzing user requirements and designing software solutions",
                                 "Writing and testing code using programming languages",
                                 "Debugging and troubleshooting software issues",
                                 "Collaborating with team members to deliver high-quality software products"],
            "Qualifications": ["Bachelor's degree in computer science, software engineering, or related field",
                              "Proficiency in programming languages such as Java, Python, or C++",
                              "Experience with software development tools and frameworks",
                              "Strong problem-solving and analytical skills"],
            "Industry Type": "Information Technology, Software Development, Computer Science"
        },
        "Mechanical Engineer": {
            "Summary": "Designs and manufactures mechanical systems and devices.",
            "Responsibilities": ["Designing mechanical components and systems",
                                 "Conducting tests and experiments to evaluate mechanical performance",
                                 "Developing prototypes and manufacturing processes",
                                 "Collaborating with engineers and technicians to solve technical challenges"],
            "Qualifications": ["Bachelor's degree in mechanical engineering or related field",
                              "Knowledge of CAD software and engineering principles",
                              "Experience with mechanical design and analysis tools",
                              "Excellent problem-solving and communication skills"],
            "Industry Type": "Engineering, Manufacturing, Automotive"
        },
        "Electrical Engineer": {
            "Summary": "Designs and develops electrical systems and equipment.",
            "Responsibilities": ["Designing electrical circuits and systems",
                                 "Testing and troubleshooting electrical components",
                                 "Developing electrical control systems and automation solutions",
                                 "Collaborating with other engineers to integrate electrical systems into larger projects"],
            "Qualifications": ["Bachelor's degree in electrical engineering or related field",
                              "Knowledge of electrical engineering principles and practices",
                              "Experience with electrical design software and testing equipment",
                              "Strong analytical and problem-solving skills"],
            "Industry Type": "Electronics, Power Generation, Automation"
        },
        "Civil Engineer": {
            "Summary": "Plans, designs, and oversees construction of infrastructure projects.",
            "Responsibilities": ["Preparing project plans and specifications",
                                 "Conducting site investigations and surveys",
                                 "Supervising construction activities and ensuring compliance with regulations",
                                 "Managing project budgets and timelines"],
            "Qualifications": ["Bachelor's degree in civil engineering or related field",
                              "Knowledge of engineering design and construction principles",
                              "Experience with CAD software and project management tools",
                              "Excellent communication and teamwork skills"],
            "Industry Type": "Construction, Infrastructure, Civil Engineering"
        },
        "Aerospace Engineer": {
            "Summary": "Designs and develops aircraft, spacecraft, and related systems.",
            "Responsibilities": ["Designing aircraft and spacecraft components",
                                 "Conducting aerodynamic analysis and simulations",
                                 "Testing prototypes and evaluating performance",
                                 "Collaborating with multidisciplinary teams to solve engineering challenges"],
            "Qualifications": ["Bachelor's degree in aerospace engineering or related field",
                              "Knowledge of aerospace engineering principles and regulations",
                              "Experience with aerospace design software and testing methods",
                              "Strong analytical and problem-solving skills"],
            "Industry Type": "Aerospace, Aviation, Defense"
        },
        "Biomedical Engineer": {
            "Summary": "Applies engineering principles to healthcare and medical technologies.",
            "Responsibilities": ["Designing medical devices and equipment",
                                 "Developing prosthetics and artificial organs",
                                 "Conducting research to improve medical technology",
                                 "Collaborating with medical professionals to identify needs and solutions"],
            "Qualifications": ["Bachelor's degree in biomedical engineering or related field",
                              "Understanding of biology and medical science principles",
                              "Experience with medical device design and regulatory requirements",
                              "Strong problem-solving and communication skills"],
            "Industry Type": "Biomedical, Healthcare, Medical Devices"
        },
        "Robotics Engineer": {
            "Summary": "Designs and builds robots and robotic systems.",
            "Responsibilities": ["Designing robotic systems and components",
                                 "Programming robots to perform specific tasks",
                                 "Testing and debugging robotic prototypes",
                                 "Collaborating with engineers and researchers on robotics projects"],
            "Qualifications": ["Bachelor's degree in robotics engineering, mechanical engineering, or related field",
                              "Knowledge of robotics principles and programming languages",
                              "Experience with robotics hardware and software",
                              "Creative problem-solving skills"],
            "Industry Type": "Robotics, Automation, Manufacturing"
        },
        "Chemical Engineer": {
            "Summary": "Designs processes and equipment for chemical manufacturing.",
            "Responsibilities": ["Developing and optimizing chemical processes",
                                 "Designing chemical reactors and equipment",
                                 "Conducting experiments and analyzing data",
                                 "Ensuring compliance with safety and environmental regulations"],
            "Qualifications": ["Bachelor's degree in chemical engineering or related field",
                              "Knowledge of chemistry and chemical engineering principles",
                              "Experience with process simulation software and laboratory techniques",
                              "Strong analytical and problem-solving skills"],
            "Industry Type": "Chemical, Manufacturing, Process Engineering"
        },
        "Automotive Engineer": {
            "Summary": "Designs and develops vehicles and automotive systems.",
            "Responsibilities": ["Designing vehicle components and systems",
                                 "Testing and evaluating automotive prototypes",
                                 "Improving vehicle performance and efficiency",
                                 "Collaborating with suppliers and manufacturers on automotive projects"],
            "Qualifications": ["Bachelor's degree in automotive engineering, mechanical engineering, or related field",
                              "Knowledge of automotive engineering principles and regulations",
                              "Experience with vehicle design software and testing methods",
                              "Passion for automobiles and innovation"],
            "Industry Type": "Automotive, Transportation, Manufacturing"
        },
        "Network Engineer": {
            "Summary": "Designs and manages computer networks and communication systems.",
            "Responsibilities": ["Designing and implementing network infrastructure",
                                 "Configuring routers, switches, and other network devices",
                                 "Monitoring network performance and troubleshooting issues",
                                 "Ensuring network security and data protection"],
            "Qualifications": ["Bachelor's degree in computer science, information technology, or related field",
                              "Certification such as Cisco Certified Network Associate (CCNA)",
                              "Experience with network protocols and technologies",
                              "Strong problem-solving and communication skills"],
            "Industry Type": "Information Technology, Telecommunications, Networking"
        }
        # Include details for other job roles in the BE or BTech UG course here
    },
    "BFA": {
        "Graphic Designer": {
            "Summary": "Creates visual concepts using computer software or by hand to communicate ideas that inspire, inform, and captivate consumers.",
            "Responsibilities": ["Meeting clients or art directors to determine the scope of a project",
                                 "Using digital illustration, photo editing software, and layout software to create designs",
                                 "Presenting designs to clients or art directors for approval",
                                 "Working with a team of illustrators, photographers, and copywriters to produce final design",
                                 "Testing graphics across various media"],
            "Qualifications": ["Bachelor's degree in graphic design or related field",
                              "Proficiency in graphic design software such as Adobe Creative Suite",
                              "Strong creativity and imagination",
                              "Excellent communication and interpersonal skills"],
            "Industry Type": "Graphic Design, Advertising, Marketing"
        },
        "Illustrator": {
            "Summary": "Creates original images for a wide range of products and mediums.",
            "Responsibilities": ["Meeting with clients to determine their needs and style",
                                 "Developing illustrations based on client requirements",
                                 "Refining designs with illustration software",
                                 "Collaborating with writers, designers, and other artists to meet project deadlines"],
            "Qualifications": ["Bachelor's degree in illustration or related field",
                              "Proficiency in illustration software such as Adobe Illustrator or Procreate",
                              "Strong drawing and artistic skills",
                              "Ability to work collaboratively and take feedback"],
            "Industry Type": "Publishing, Advertising, Animation"
        },
        "Art Director": {
            "Summary": "Responsible for the visual style and images in magazines, newspapers, product packaging, and movie and television productions.",
            "Responsibilities": ["Developing visual concepts and guidelines",
                                 "Overseeing design projects from conception to completion",
                                 "Approving designs, artwork, and photography",
                                 "Collaborating with clients, writers, and other artists"],
            "Qualifications": ["Bachelor's degree in graphic design, fine arts, or related field",
                              "Extensive experience in graphic design or art direction",
                              "Strong leadership and communication skills",
                              "Ability to manage multiple projects and meet deadlines"],
            "Industry Type": "Advertising, Publishing, Film"
        },
        "Animator": {
            "Summary": "Creates animation and visual effects for films, television, video games, and other forms of media.",
            "Responsibilities": ["Developing storyboards and animation concepts",
                                 "Creating 2D or 3D animation sequences",
                                 "Collaborating with directors, designers, and other animators",
                                 "Ensuring animation meets quality standards and project deadlines"],
            "Qualifications": ["Bachelor's degree in animation, fine arts, or related field",
                              "Proficiency in animation software such as Adobe After Effects, Maya, or Blender",
                              "Strong drawing and storytelling skills",
                              "Ability to work in a collaborative environment"],
            "Industry Type": "Animation, Film, Video Games"
        },
        "Multimedia Artist": {
            "Summary": "Creates special effects, animation, or other visual images using film, video, computers, or other electronic tools and media for use in products or creations, such as computer games, movies, music videos, and commercials.",
            "Responsibilities": ["Generating and developing multimedia designs",
                                 "Creating 2D and 3D animations, graphics, and special effects",
                                 "Collaborating with clients, directors, and other artists",
                                 "Editing and revising multimedia content as needed"],
            "Qualifications": ["Bachelor's degree in multimedia design, animation, or related field",
                              "Proficiency in multimedia software such as Adobe Creative Suite, Autodesk Maya, or Cinema 4D",
                              "Strong artistic and technical skills",
                              "Ability to work under pressure and meet tight deadlines"],
            "Industry Type": "Multimedia, Entertainment, Advertising"
        },
        "Film and Video Editor": {
            "Summary": "Edits moving images on film, video, or other media.",
            "Responsibilities": ["Editing film or video footage using editing software",
                                 "Assembling raw footage and applying artistic and technical skills to create polished final products",
                                 "Collaborating with directors, producers, and other team members",
                                 "Ensuring the final product meets quality standards and project requirements"],
            "Qualifications": ["Bachelor's degree in film studies, media production, or related field",
                              "Proficiency in video editing software such as Adobe Premiere Pro, Final Cut Pro, or Avid Media Composer",
                              "Strong storytelling and visual storytelling skills",
                              "Ability to work under tight deadlines and in a collaborative environment"],
            "Industry Type": "Film, Television, Advertising"
        },
        "Photographer": {
            "Summary": "Captures and edits photographic images for a wide range of creative, technical, and documentary purposes.",
            "Responsibilities": ["Planning and conducting photo shoots",
                                 "Selecting and editing images to meet client or project requirements",
                                 "Collaborating with clients, art directors, and other team members",
                                 "Maintaining and managing equipment"],
            "Qualifications": ["Bachelor's degree in photography, visual arts, or related field",
                              "Proficiency in digital photography and editing software such as Adobe Photoshop or Lightroom",
                              "Strong artistic vision and technical skills",
                              "Ability to work in various lighting conditions and settings"],
            "Industry Type": "Photography, Advertising, Media"
        },
        "Interior Designer": {
            "Summary": "Plans and designs interior spaces for homes, businesses, and other environments.",
            "Responsibilities": ["Consulting with clients to determine design preferences and requirements",
                                 "Developing design concepts and plans",
                                 "Selecting materials, furniture, and fixtures",
                                 "Coordinating with architects, contractors, and other professionals"],
            "Qualifications": ["Bachelor's degree in interior design or related field",
                              "Proficiency in design software such as AutoCAD, SketchUp, or Revit",
                              "Strong creativity and design skills",
                              "Knowledge of building codes and regulations"],
            "Industry Type": "Interior Design, Architecture, Real Estate"
        },
        "Art Teacher": {
            "Summary": "Instructs students in various forms of visual arts, such as drawing, painting, and sculpture.",
            "Responsibilities": ["Planning and delivering art lessons",
                                 "Demonstrating techniques and methods",
                                 "Providing constructive feedback and guidance to students",
                                 "Evaluating student work and progress"],
            "Qualifications": ["Bachelor's degree in art education, fine arts, or related field",
                              "Teaching certification or licensure (may vary by location)",
                              "Strong artistic skills and knowledge",
                              "Effective communication and classroom management skills"],
            "Industry Type": "Education, Fine Arts, Community Centers"
        },
        "Gallery Curator": {
            "Summary": "Manages and oversees art collections in galleries, museums, or other cultural institutions.",
            "Responsibilities": ["Acquiring and cataloging art pieces",
                                 "Planning and organizing exhibitions and events",
                                 "Promoting and marketing gallery activities",
                                 "Collaborating with artists, collectors, and donors"],
            "Qualifications": ["Bachelor's degree in art history, museum studies, or related field",
                              "Experience in art curation or gallery management",
                              "Knowledge of art history and contemporary art trends",
                              "Excellent organizational and communication skills"],
            "Industry Type": "Art Galleries, Museums, Cultural Institutions"
        }
        # Include details for other job roles in the BFA course here
    },
  "BBA":{
           "Marketing Manager": {
            "Summary": "Plans and executes marketing strategies to promote products or services and achieve business objectives.",
            "Responsibilities": [
                "Developing marketing plans and strategies",
                "Conducting market research and analysis",
                "Managing advertising and promotional campaigns",
                "Monitoring and analyzing campaign performance",
                "Collaborating with sales, product, and creative teams"
            ],
            "Qualifications": [
                "Bachelor's degree in marketing, business administration, or related field",
                "Strong analytical and strategic thinking skills",
                "Excellent communication and interpersonal skills",
                "Experience in marketing or related roles"
            ],
            "Industry Type": "Marketing, Advertising, Sales"
        },
        "Financial Analyst": {
            "Summary": "Analyzes financial data and market trends to provide insights and recommendations for investment decisions, budgeting, and financial planning.",
            "Responsibilities": [
                "Conducting financial analysis and forecasting",
                "Preparing financial reports and presentations",
                "Assessing investment opportunities and risks",
                "Monitoring industry and market trends",
                "Providing financial guidance and recommendations"
            ],
            "Qualifications": [
                "Bachelor's degree in finance, accounting, economics, or related field",
                "Strong analytical and quantitative skills",
                "Proficiency in financial modeling and analysis tools",
                "Knowledge of financial regulations and reporting standards"
            ],
            "Industry Type": "Finance, Investment, Banking"
        },
        "Operations Manager": {
            "Summary": "Oversees the operational activities of a company or organization to ensure efficient and effective processes and resource utilization.",
            "Responsibilities": [
                "Developing and implementing operational policies and procedures",
                "Managing day-to-day operations and workflow",
                "Optimizing processes to improve efficiency and productivity",
                "Monitoring and analyzing operational performance metrics",
                "Leading and supervising operational staff"
            ],
            "Qualifications": [
                "Bachelor's degree in business administration, operations management, or related field",
                "Strong leadership and decision-making skills",
                "Excellent organizational and problem-solving abilities",
                "Experience in operations management or related roles"
            ],
            "Industry Type": "Business Operations, Manufacturing, Services"
        },
        "Human Resources Manager": {
            "Summary": "Plans, directs, and coordinates the administrative functions of an organization's human resources department.",
            "Responsibilities": [
                "Developing and implementing HR policies and procedures",
                "Recruiting and hiring employees",
                "Managing employee benefits and compensation",
                "Providing employee training and development programs",
                "Resolving employee relations issues"
            ],
            "Qualifications": [
                "Bachelor's degree in human resources management, business administration, or related field",
                "Knowledge of HR laws, regulations, and best practices",
                "Strong interpersonal and communication skills",
                "Experience in human resources management"
            ],
            "Industry Type": "Human Resources, Business Administration"
        },
        "Business Development Manager": {
            "Summary": "Identifies and develops business opportunities to drive revenue growth and expand the company's market presence.",
            "Responsibilities": [
                "Identifying new business opportunities and partnerships",
                "Building and maintaining relationships with clients and stakeholders",
                "Developing and implementing sales strategies",
                "Negotiating contracts and agreements",
                "Analyzing market trends and competitors"
            ],
            "Qualifications": [
                "Bachelor's degree in business administration, marketing, or related field",
                "Strong sales and negotiation skills",
                "Excellent communication and interpersonal abilities",
                "Experience in business development or sales"
            ],
            "Industry Type": "Business Development, Sales, Consulting"
        },
        "Sales Manager": {
            "Summary": "Leads and manages a sales team to achieve sales targets and objectives for the company's products or services.",
            "Responsibilities": [
                "Setting sales goals and targets",
                "Recruiting, training, and managing sales staff",
                "Developing sales strategies and plans",
                "Monitoring and analyzing sales performance",
                "Building and maintaining client relationships"
            ],
            "Qualifications": [
                "Bachelor's degree in business administration, marketing, or related field",
                "Proven track record in sales management",
                "Strong leadership and motivational skills",
                "Excellent communication and negotiation abilities"
            ],
            "Industry Type": "Sales, Marketing, Retail"
        },
        "Project Manager": {
            "Summary": "Plans, coordinates, and oversees projects to ensure they are completed on time, within budget, and according to specifications.",
            "Responsibilities": [
                "Defining project scope, goals, and deliverables",
                "Creating project plans and schedules",
                "Allocating resources and managing budgets",
                "Monitoring project progress and performance",
                "Managing project team and stakeholders"
            ],
            "Qualifications": [
                "Bachelor's degree in project management, business administration, or related field",
                "Project management certification (e.g., PMP) is often preferred",
                "Strong organizational and leadership skills",
                "Experience in project management"
            ],
            "Industry Type": "Project Management, Construction, Information Technology"
        },
        "Management Consultant": {
            "Summary": "Provides expert advice and guidance to businesses and organizations to improve performance, solve problems, and implement strategic initiatives.",
            "Responsibilities": [
                "Conducting research and analysis to identify business problems",
                "Developing recommendations and solutions",
                "Assisting in the implementation of strategic plans",
                "Providing guidance on organizational change and improvement",
                "Communicating findings and recommendations to clients"
            ],
            "Qualifications": [
                "Bachelor's degree in business administration, management, or related field",
                "Strong analytical and problem-solving skills",
                "Excellent communication and presentation abilities",
                "Experience in consulting or relevant industries"
            ],
            "Industry Type": "Consulting, Business Services, Management"
        },
        "Entrepreneur": {
            "Summary": "Initiates, manages, and assumes the risks of a business venture with the goal of creating value and achieving financial success.",
            "Responsibilities": [
                "Identifying business opportunities and concepts",
                "Developing business plans and strategies",
                "Securing funding and resources",
                "Managing operations and finances",
                "Adapting to market changes and challenges"
            ],
            "Qualifications": [
                "Bachelor's degree in business administration, entrepreneurship, or related field",
                "Strong leadership and decision-making skills",
                "Risk-taking attitude and ability to innovate",
                "Experience in starting and running a business"
            ],
            "Industry Type": "Entrepreneurship, Startups, Business"
        },"Supply Chain Manager": {
        "Summary": "Responsible for overseeing and managing the entire supply chain process, from procurement of raw materials to delivery of finished products, ensuring efficiency and cost-effectiveness.",
        "Responsibilities": [
            "Developing and implementing supply chain strategies to optimize efficiency and reduce costs",
            "Managing procurement of raw materials, inventory levels, and supplier relationships",
            "Coordinating logistics, including transportation, warehousing, and distribution",
            "Analyzing data and trends to forecast demand and make informed decisions",
            "Ensuring compliance with regulations and quality standards",
            "Identifying areas for improvement and implementing process enhancements"
        ],
        "Qualifications": [
            "Bachelor's degree in supply chain management, logistics, business administration, or related field",
            "Proven experience in supply chain management or logistics",
            "Strong analytical and problem-solving skills",
            "Excellent communication and negotiation abilities",
            "Proficiency in supply chain management software and tools"
        ],
        "Industry Type": "Supply Chain, Logistics, Manufacturing"
    }
  },
  "BArch": {
    "Architect": {
        "Summary": "Designs and plans the construction of buildings and structures, considering both aesthetic and functional aspects.",
        "Responsibilities": [
            "Creating architectural designs and plans based on client requirements and budget constraints",
            "Conducting site visits and surveys to assess environmental factors",
            "Collaborating with engineers, contractors, and clients to ensure project feasibility and compliance with regulations",
            "Using computer-aided design (CAD) software to develop detailed drawings and models",
            "Managing construction projects and overseeing the implementation of architectural plans"
        ],
        "Qualifications": [
            "Bachelor's degree in architecture",
            "Professional licensure or certification",
            "Proficiency in CAD software and other design tools",
            "Strong design and spatial planning skills",
            "Knowledge of building codes and regulations"
        ],
        "Industry Type": "Architecture, Construction, Engineering"
    },
    "Urban Planner": {
        "Summary": "Develops plans and programs for land use in urban areas, considering factors such as population growth, transportation, and environmental impact.",
        "Responsibilities": [
            "Conducting research and analysis to assess community needs and demographic trends",
            "Developing comprehensive plans for land use, zoning, and transportation",
            "Engaging with stakeholders and community members to gather input and support for planning initiatives",
            "Evaluating the impact of proposed development projects on the surrounding environment and infrastructure",
            "Collaborating with architects, engineers, and policymakers to implement urban planning initiatives"
        ],
        "Qualifications": [
            "Bachelor's degree in urban planning, geography, or related field",
            "Strong analytical and research skills",
            "Knowledge of urban planning principles and regulations",
            "Excellent communication and interpersonal skills",
            "Proficiency in GIS and urban planning software"
        ],
        "Industry Type": "Urban Planning, Government, Consulting"
    },
    "Interior Designer": {
        "Summary": "Plans and designs interior spaces for homes, businesses, and other environments, focusing on aesthetics, functionality, and safety.",
        "Responsibilities": [
            "Consulting with clients to determine design preferences, functional requirements, and budget constraints",
            "Developing design concepts and plans that integrate aesthetic and functional elements",
            "Selecting materials, furniture, and fixtures to enhance the overall design concept",
            "Collaborating with architects, contractors, and other professionals to ensure design feasibility and compliance with regulations",
            "Overseeing the implementation of interior design plans and coordinating with contractors and suppliers"
        ],
        "Qualifications": [
            "Bachelor's degree in interior design or related field",
            "Strong creativity and design skills",
            "Proficiency in CAD software and other design tools",
            "Knowledge of building codes and safety standards",
            "Effective communication and project management abilities"
        ],
        "Industry Type": "Interior Design, Architecture, Real Estate"
    },
    "Landscape Architect": {
        "Summary": "Designs outdoor spaces, parks, gardens, and recreational areas, considering factors such as environmental sustainability, aesthetics, and functionality.",
        "Responsibilities": [
            "Assessing site conditions, including topography, soil quality, and existing vegetation",
            "Developing landscape designs and plans that meet client needs and project goals",
            "Selecting appropriate plants, materials, and construction techniques for landscape projects",
            "Collaborating with architects, engineers, and environmental scientists to ensure design feasibility and sustainability",
            "Managing landscape construction projects and overseeing the implementation of design plans"
        ],
        "Qualifications": [
            "Bachelor's degree in landscape architecture or related field",
            "Professional licensure or certification",
            "Strong design and technical skills",
            "Knowledge of environmental regulations and sustainable design principles",
            "Excellent communication and collaboration abilities"
        ],
        "Industry Type": "Landscape Architecture, Environmental Planning, Construction"
    },
    "Construction Manager": {
        "Summary": "Oversees and manages construction projects, including planning, budgeting, scheduling, and coordination of subcontractors and workers.",
        "Responsibilities": [
            "Developing project plans, budgets, and schedules",
            "Coordinating and supervising construction activities, subcontractors, and workers",
            "Ensuring compliance with building codes, safety regulations, and project specifications",
            "Managing project finances, including cost estimation, budget tracking, and procurement",
            "Communicating with clients, architects, engineers, and other stakeholders to provide project updates and address concerns"
        ],
        "Qualifications": [
            "Bachelor's degree in construction management, civil engineering, or related field",
            "Relevant work experience in construction project management",
            "Strong leadership and organizational skills",
            "Knowledge of construction methods, materials, and regulations",
            "Proficiency in project management software"
        ],
        "Industry Type": "Construction, Engineering, Real Estate"
    },
    "Sustainability Consultant": {
        "Summary": "Advises organizations on sustainable practices and strategies to minimize environmental impact and enhance resource efficiency.",
        "Responsibilities": [
            "Conducting sustainability assessments and audits to identify opportunities for improvement",
            "Developing and implementing sustainability initiatives, such as energy efficiency programs and waste reduction strategies",
            "Analyzing data and trends to evaluate the environmental performance of organizations and projects",
            "Providing training and education to staff and stakeholders on sustainable practices",
            "Collaborating with clients, architects, engineers, and policymakers to integrate sustainability into projects and operations"
        ],
        "Qualifications": [
            "Bachelor's degree in environmental science, sustainability, engineering, or related field",
            "Relevant experience in sustainability consulting or environmental management",
            "Knowledge of sustainable design principles and green building standards",
            "Strong analytical and problem-solving skills",
            "Excellent communication and presentation abilities"
        ],
        "Industry Type": "Environmental Consulting, Sustainability, Engineering"
    },
    "Historic Preservationist": {
        "Summary": "Works to protect and preserve historic buildings, structures, and sites, ensuring their cultural significance and architectural integrity are maintained.",
        "Responsibilities": [
            "Conducting historical research and documentation to assess the significance of historic resources",
            "Developing preservation plans and strategies for historic buildings and sites",
            "Collaborating with architects, engineers, and government agencies to ensure compliance with preservation standards and regulations",
            "Providing technical assistance and guidance to property owners, developers, and community organizations",
            "Promoting public awareness and appreciation of historic preservation through education and outreach initiatives"
        ],
        "Qualifications": [
            "Bachelor's degree in historic preservation, architecture, history, or related field",
            "Knowledge of preservation principles, practices, and regulations",
            "Experience in historic research, documentation, and evaluation",
            "Strong communication and advocacy skills",
            "Ability to work collaboratively with diverse stakeholders"
        ],
        "Industry Type": "Historic Preservation, Architecture, Government"
    },
    "Building Inspector": {
        "Summary": "Evaluates buildings and structures to ensure compliance with building codes, zoning regulations, and safety standards.",
        "Responsibilities": [
            "Conducting inspections of buildings and construction sites to assess compliance with codes and regulations",
            "Identifying code violations, safety hazards, and structural deficiencies",
            "Preparing inspection reports and documenting findings with photographs and detailed notes",
            "Communicating findings and recommendations to property owners, contractors, and government officials",
            "Providing guidance and assistance to address code violations and ensure compliance"
        ],
        "Qualifications": [
            "Bachelor's degree in architecture, engineering, construction management, or related field",
            "Professional certification or licensure as a building inspector",
            "Knowledge of building codes, zoning regulations, and construction practices",
            "Attention to detail and strong observational skills",
            "Effective communication and interpersonal abilities"
        ],
        "Industry Type": "Construction, Building Inspection, Government"
    },
    "CAD Technician": {
        "Summary": "Creates detailed technical drawings and plans using computer-aided design (CAD) software for architects, engineers, and construction professionals.",
        "Responsibilities": [
            "Developing architectural, structural, and mechanical drawings based on design specifications",
            "Collaborating with architects, engineers, and other professionals to ensure accuracy and completeness of drawings",
            "Modifying and revising drawings as needed to accommodate changes and updates",
            "Maintaining organized electronic files and documentation for drawing revisions and project archives",
            "Providing technical support and assistance to project teams and clients"
        ],
        "Qualifications": [
            "Bachelor's degree in drafting, engineering, architecture, or related field",
            "Proficiency in CAD software such as AutoCAD, Revit, or SolidWorks",
            "Knowledge of drafting standards and practices",
            "Attention to detail and accuracy in technical drawings",
            "Strong problem-solving and communication skills"
        ],
        "Industry Type": "Architecture, Engineering, Construction"
    },
    "Real Estate Developer": {
        "Summary": "Identifies, acquires, and develops real estate properties for residential, commercial, or mixed-use projects.",
        "Responsibilities": [
            "Conducting market research and feasibility studies to identify potential real estate development opportunities",
            "Acquiring land, securing financing, and obtaining necessary permits and approvals for development projects",
            "Collaborating with architects, engineers, contractors, and other professionals to design and develop properties",
            "Managing construction activities, budgeting, and scheduling to ensure project success",
            "Marketing and selling or leasing completed properties to investors, buyers, or tenants"
        ],
        "Qualifications": [
            "Bachelor's degree in real estate development, finance, business administration, or related field",
            "Relevant experience in real estate development, investment, or finance",
            "Knowledge of real estate market trends, property valuation, and development processes",
            "Strong financial analysis and project management skills",
            "Excellent negotiation and interpersonal abilities"
        ],
        "Industry Type": "Real Estate Development, Property Management, Construction"
    }
},
"BCA": {
    "Software Developer": {
        "Summary": "Designs, develops, and tests software applications to meet specific user needs and business requirements.",
        "Responsibilities": [
            "Analyzing user requirements and designing software solutions",
            "Writing and debugging code using programming languages such as Java, Python, or C++",
            "Testing and debugging software to ensure functionality and performance",
            "Collaborating with team members and stakeholders to deliver high-quality software products",
            "Maintaining and updating software applications to address issues and add new features"
        ],
        "Qualifications": [
            "Bachelor's degree in computer science, software engineering, or related field",
            "Proficiency in programming languages and development tools",
            "Strong problem-solving and analytical skills",
            "Ability to work in a team environment and communicate effectively",
            "Knowledge of software development lifecycle (SDLC) methodologies"
        ],
        "Industry Type": "Software Development, Information Technology, Consulting"
    },
    "Database Administrator": {
        "Summary": "Manages and maintains databases to ensure data integrity, security, and accessibility for users and applications.",
        "Responsibilities": [
            "Installing, configuring, and upgrading database software and related components",
            "Creating and maintaining database structures, tables, and views",
            "Monitoring database performance and optimizing query performance",
            "Implementing data security measures to protect sensitive information",
            "Troubleshooting database issues and performing backups and recovery"
        ],
        "Qualifications": [
            "Bachelor's degree in computer science, information technology, or related field",
            "Certification in database administration (e.g., Oracle Certified Professional)",
            "Knowledge of database management systems such as Oracle, SQL Server, or MySQL",
            "Strong understanding of database design and data normalization principles",
            "Excellent problem-solving and communication skills"
        ],
        "Industry Type": "Database Management, Information Technology, Finance"
    },
    "Web Developer": {
        "Summary": "Designs and develops websites and web applications using programming languages, frameworks, and tools.",
        "Responsibilities": [
            "Creating web page layouts and user interfaces using HTML, CSS, and JavaScript",
            "Developing server-side code and databases for web applications",
            "Integrating third-party services and APIs into web applications",
            "Testing and debugging web applications for performance and usability",
            "Collaborating with designers, developers, and stakeholders to deliver high-quality web solutions"
        ],
        "Qualifications": [
            "Bachelor's degree in computer science, web development, or related field",
            "Proficiency in web development languages and frameworks (e.g., React, Angular, Node.js)",
            "Experience with front-end and back-end development technologies",
            "Knowledge of web standards and best practices for accessibility and usability",
            "Strong problem-solving and teamwork skills"
        ],
        "Industry Type": "Web Development, Information Technology, E-commerce"
    },
    "Network Administrator": {
        "Summary": "Manages and maintains computer networks to ensure connectivity, security, and performance for users and applications.",
        "Responsibilities": [
            "Installing, configuring, and maintaining network hardware and software components",
            "Monitoring network performance and optimizing network infrastructure",
            "Implementing network security measures to protect against unauthorized access and cyber threats",
            "Troubleshooting network issues and performing regular maintenance tasks",
            "Collaborating with IT teams and vendors to plan and implement network upgrades and expansions"
        ],
        "Qualifications": [
            "Bachelor's degree in computer science, information technology, or related field",
            "Certification in networking technologies (e.g., Cisco Certified Network Associate)",
            "Experience with network protocols, routing, and switching technologies",
            "Knowledge of network security principles and best practices",
            "Strong analytical and problem-solving skills"
        ],
        "Industry Type": "Network Administration, Information Technology, Telecommunications"
    },
    "Systems Analyst": {
        "Summary": "Analyzes business requirements and IT systems to design and implement solutions that improve efficiency, productivity, and performance.",
        "Responsibilities": [
            "Gathering and analyzing user requirements and system specifications",
            "Designing and documenting system architectures and workflows",
            "Evaluating existing IT systems and proposing enhancements or replacements",
            "Collaborating with stakeholders and IT teams to implement system changes and upgrades",
            "Testing and debugging system components to ensure functionality and performance"
        ],
        "Qualifications": [
            "Bachelor's degree in computer science, information systems, or related field",
            "Strong analytical and problem-solving skills",
            "Experience with system analysis and design methodologies",
            "Knowledge of business process modeling and workflow analysis",
            "Excellent communication and interpersonal abilities"
        ],
        "Industry Type": "Information Technology, Consulting, Finance"
    },
    "IT Consultant": {
        "Summary": "Provides strategic advice and technical expertise to help organizations optimize their IT systems and infrastructure.",
        "Responsibilities": [
            "Assessing clients' IT systems and infrastructure to identify opportunities for improvement",
            "Developing IT strategies, roadmaps, and implementation plans",
            "Providing technical guidance and support for IT projects and initiatives",
            "Evaluating emerging technologies and recommending solutions that align with client objectives",
            "Delivering presentations and reports to communicate findings and recommendations to clients"
        ],
        "Qualifications": [
            "Bachelor's degree in computer science, information technology, or related field",
            "Proven experience in IT consulting or systems integration",
            "Strong understanding of IT systems and infrastructure",
            "Excellent problem-solving and decision-making skills",
            "Effective communication and presentation abilities"
        ],
        "Industry Type": "IT Consulting, Information Technology, Business Services"
    },
    "Game Developer": {
        "Summary": "Designs and develops video games for various platforms, including consoles, PCs, and mobile devices.",
        "Responsibilities": [
            "Creating game concepts, storylines, and characters",
            "Developing game mechanics, levels, and user interfaces",
            "Programming game logic and behavior using game engines and scripting languages",
            "Testing and debugging games to ensure functionality and performance",
            "Collaborating with artists, designers, and other developers to create immersive gaming experiences"
        ],
        "Qualifications": [
            "Bachelor's degree in computer science, game development, or related field",
            "Proficiency in game development tools and programming languages (e.g., Unity, C#, Unreal Engine)",
            "Strong problem-solving and creative thinking skills",
            "Passion for gaming and understanding of game design principles",
            "Ability to work effectively in a team environment"
        ],
        "Industry Type": "Video Game Development, Entertainment, Software"
    },
    "Computer Programmer": {
        "Summary": "Writes, tests, and maintains computer programs and software applications to solve problems and meet specific user needs.",
        "Responsibilities": [
            "Analyzing user requirements and designing software solutions",
            "Writing, debugging, and testing code using programming languages such as Java, Python, or C++",
            "Documenting program functionality and code changes for reference and future maintenance",
            "Collaborating with other programmers and software engineers to develop complex systems",
            "Troubleshooting and resolving software defects and issues"
        ],
        "Qualifications": [
            "Bachelor's degree in computer science, software engineering, or related field",
            "Proficiency in programming languages and development tools",
            "Strong problem-solving and analytical skills",
            "Ability to work independently and in a team environment",
            "Knowledge of software development best practices and methodologies"
        ],
        "Industry Type": "Software Development, Information Technology, Consulting"
    },
    "UI/UX Designer": {
        "Summary": "Designs user interfaces and experiences for software applications, websites, and digital products to enhance usability and user satisfaction.",
        "Responsibilities": [
            "Conducting user research and gathering feedback to inform design decisions",
            "Creating wireframes, prototypes, and mockups to visualize design concepts",
            "Designing intuitive and engaging user interfaces for web and mobile applications",
            "Collaborating with developers and stakeholders to implement and iterate on designs",
            "Testing and refining designs based on user feedback and usability testing"
        ],
        "Qualifications": [
            "Bachelor's degree in graphic design, human-computer interaction, or related field",
            "Proficiency in design tools such as Sketch, Adobe XD, or Figma",
            "Understanding of user-centered design principles and best practices",
            "Strong visual and interactive design skills",
            "Excellent communication and collaboration abilities"
        ],
        "Industry Type": "UI/UX Design, Web Development, Software"
    },
    "Cybersecurity Analyst": {
        "Summary": "Protects computer systems and networks from cyber threats by implementing security measures, monitoring for vulnerabilities, and responding to incidents.",
        "Responsibilities": [
            "Conducting security assessments and risk analyses to identify vulnerabilities and threats",
            "Implementing security controls and measures to protect against cyber attacks and breaches",
            "Monitoring security systems and networks for suspicious activity and potential threats",
            "Investigating security incidents and responding to breaches in a timely manner",
            "Educating users and stakeholders on cybersecurity best practices and policies"
        ],
        "Qualifications": [
            "Bachelor's degree in cybersecurity, computer science, or related field",
            "Certifications such as Certified Information Systems Security Professional (CISSP) or Certified Ethical Hacker (CEH)",
            "Experience with cybersecurity tools and technologies (e.g., firewalls, intrusion detection systems)",
            "Knowledge of cybersecurity frameworks and standards (e.g., NIST, ISO 27001)",
            "Strong problem-solving and analytical skills"
        ],
        "Industry Type": "Cybersecurity, Information Technology, Government"
    }
},
"BEd": {
    "Teacher": {
        "Summary": "Educates students in various subjects and helps them develop cognitive, social, and emotional skills.",
        "Responsibilities": [
            "Planning and delivering lessons based on curriculum guidelines",
            "Assessing student progress and adjusting teaching methods accordingly",
            "Creating a positive and inclusive learning environment",
            "Collaborating with colleagues, parents, and administrators to support student learning",
            "Providing feedback and guidance to students to help them achieve academic success"
        ],
        "Qualifications": [
            "Bachelor's degree in education or related field",
            "Teaching certification or licensure (varies by location)",
            "Strong subject-area knowledge and pedagogical skills",
            "Effective communication and classroom management abilities",
            "Passion for working with students and facilitating their learning"
        ],
        "Industry Type": "Education, Schools, Nonprofit Organizations"
    },
    "School Counselor": {
        "Summary": "Provides academic, career, and personal counseling to students to help them achieve academic success and personal well-being.",
        "Responsibilities": [
            "Assisting students in developing academic and career plans",
            "Providing individual and group counseling sessions to address personal and social issues",
            "Assessing student needs and making referrals to outside resources as needed",
            "Collaborating with teachers, parents, and administrators to support student development",
            "Promoting a positive school climate and implementing programs to address student needs"
        ],
        "Qualifications": [
            "Master's degree in school counseling or related field",
            "Licensure or certification as a school counselor (varies by location)",
            "Knowledge of counseling techniques and theories",
            "Strong interpersonal and communication skills",
            "Ability to maintain confidentiality and build trust with students"
        ],
        "Industry Type": "Education, Schools, Counseling Services"
    },
    "Education Administrator": {
        "Summary": "Manages school operations and leads efforts to improve educational programs and outcomes.",
        "Responsibilities": [
            "Developing and implementing educational policies and programs",
            "Supervising teachers, staff, and other school personnel",
            "Managing school budgets, facilities, and resources",
            "Evaluating and improving curriculum standards and instructional methods",
            "Collaborating with stakeholders to set and achieve school goals"
        ],
        "Qualifications": [
            "Master's degree in education administration or related field",
            "Administrative certification or licensure (varies by location)",
            "Experience in teaching or school administration",
            "Leadership and decision-making skills",
            "Effective communication and interpersonal abilities"
        ],
        "Industry Type": "Education, Schools, Government"
    },
    "Curriculum Developer": {
        "Summary": "Designs and develops curriculum materials and instructional resources to support student learning and achievement.",
        "Responsibilities": [
            "Researching educational standards and best practices",
            "Designing and sequencing learning objectives and activities",
            "Creating instructional materials, lesson plans, and assessments",
            "Evaluating and revising curriculum based on feedback and assessment data",
            "Collaborating with teachers, administrators, and subject-matter experts"
        ],
        "Qualifications": [
            "Bachelor's or master's degree in education or related field",
            "Knowledge of curriculum development principles and practices",
            "Experience in teaching or instructional design",
            "Strong organizational and project management skills",
            "Ability to work collaboratively and communicate effectively"
        ],
        "Industry Type": "Education, Publishing, Curriculum Development"
    },
    "Instructional Designer": {
        "Summary": "Creates and implements instructional materials and learning experiences to support effective teaching and learning.",
        "Responsibilities": [
            "Analyzing learning needs and designing instructional solutions",
            "Developing learning objectives, activities, and assessments",
            "Selecting and integrating instructional technologies and resources",
            "Evaluating the effectiveness of instructional materials and making improvements",
            "Collaborating with subject-matter experts and educators"
        ],
        "Qualifications": [
            "Bachelor's or master's degree in instructional design, education, or related field",
            "Knowledge of instructional design models and theories",
            "Proficiency in instructional design software and tools",
            "Experience in curriculum development or educational technology",
            "Strong analytical and problem-solving skills"
        ],
        "Industry Type": "Education, E-learning, Corporate Training"
    },
    "Education Consultant": {
        "Summary": "Provides expertise and advice to schools, educators, and organizations to improve educational programs, policies, and practices.",
        "Responsibilities": [
            "Assessing educational needs and challenges",
            "Developing and implementing strategies for improvement",
            "Providing professional development and training for educators",
            "Evaluating and monitoring program effectiveness",
            "Collaborating with stakeholders to achieve educational goals"
        ],
        "Qualifications": [
            "Master's degree in education, educational leadership, or related field",
            "Experience in teaching, school administration, or educational consulting",
            "Knowledge of educational theories, policies, and practices",
            "Strong communication and presentation skills",
            "Ability to work collaboratively and lead change initiatives"
        ],
        "Industry Type": "Education, Consulting, Nonprofit Organizations"
    },
    "Special Education Teacher": {
        "Summary": "Educates students with special needs and provides support to help them achieve academic and personal success.",
        "Responsibilities": [
            "Developing and implementing individualized education plans (IEPs)",
            "Adapting curriculum materials and teaching strategies to meet student needs",
            "Assessing student progress and adjusting instruction accordingly",
            "Collaborating with parents, specialists, and support staff to address student needs",
            "Advocating for students with disabilities and promoting inclusive practices"
        ],
        "Qualifications": [
            "Bachelor's or master's degree in special education or related field",
            "Teaching certification or licensure with special education endorsement",
            "Knowledge of special education laws, regulations, and best practices",
            "Patience, empathy, and strong interpersonal skills",
            "Ability to differentiate instruction and support diverse learners"
        ],
        "Industry Type": "Education, Special Education Services, Nonprofit Organizations"
    },
    "ESL Teacher": {
        "Summary": "Teaches English language skills to non-native speakers to help them develop proficiency for academic, professional, and social purposes.",
        "Responsibilities": [
            "Planning and delivering ESL instruction based on language proficiency levels",
            "Developing and adapting curriculum materials and assessments",
            "Creating a supportive and engaging learning environment",
            "Providing language support and feedback to students",
            "Collaborating with colleagues and administrators to support English language learners"
        ],
        "Qualifications": [
            "Bachelor's or master's degree in ESL, TESOL, or related field",
            "ESL teaching certification or endorsement",
            "Knowledge of second language acquisition theories and teaching methods",
            "Cultural sensitivity and empathy for English language learners",
            "Effective communication and instructional skills"
        ],
        "Industry Type": "Education, Language Instruction, Nonprofit Organizations"
    },
    "School Librarian": {
        "Summary": "Manages library resources and services to support student learning, research, and literacy development.",
        "Responsibilities": [
            "Selecting and acquiring library materials and resources",
            "Organizing and cataloging library collections",
            "Assisting students and staff with research and information needs",
            "Promoting reading and literacy through programs and activities",
            "Collaborating with teachers to integrate library resources into curriculum"
        ],
        "Qualifications": [
            "Master's degree in library science or information science",
            "Certification or licensure as a school librarian (varies by location)",
            "Knowledge of library management systems and information retrieval tools",
            "Strong customer service and communication skills",
            "Passion for reading and promoting lifelong learning"
        ],
        "Industry Type": "Education, Libraries, Information Services"
    },
    "Tutor": {
        "Summary": "Provides academic support and instruction to students on a one-on-one or small group basis.",
        "Responsibilities": [
            "Assessing student learning needs and developing individualized learning plans",
            "Delivering instruction in specific subjects or skill areas",
            "Monitoring student progress and providing feedback",
            "Adapting teaching strategies to meet student needs and learning styles",
            "Communicating with parents or guardians about student progress"
        ],
        "Qualifications": [
            "Bachelor's degree in education, subject area, or related field",
            "Teaching certification or tutoring experience (preferred)",
            "Expertise in specific subject areas or academic skills",
            "Strong communication and interpersonal skills",
            "Patience, empathy, and enthusiasm for helping students learn"
        ],
        "Industry Type": "Education, Tutoring, Academic Support Services"
    }
},
"BSA": {
    "Space Artist": {
        "Summary": "Creates visual artwork inspired by space exploration, celestial bodies, and the mysteries of the universe.",
        "Responsibilities": [
            "Producing paintings, illustrations, or digital art featuring space themes",
            "Collaborating with scientists and researchers to accurately depict astronomical phenomena",
            "Participating in space-themed exhibitions and events",
            "Inspiring public interest and engagement in space exploration through art"
        ],
        "Qualifications": [
            "Bachelor's degree in fine arts, digital arts, or related field",
            "Strong artistic skills and creativity",
            "Interest in space science and astronomy",
            "Ability to collaborate with scientists and researchers",
            "Experience with various art mediums and techniques"
        ],
        "Industry Type": "Fine Arts, Astronomy, Science Communication"
    },
    "Spacecraft Designer": {
        "Summary": "Designs and engineers spacecraft and space vehicles for exploration, research, and commercial purposes.",
        "Responsibilities": [
            "Developing spacecraft concepts and designs",
            "Creating detailed engineering drawings and specifications",
            "Collaborating with aerospace engineers and scientists to integrate systems and technologies",
            "Testing and evaluating spacecraft prototypes",
            "Ensuring compliance with safety, performance, and regulatory standards"
        ],
        "Qualifications": [
            "Bachelor's or master's degree in aerospace engineering or related field",
            "Proficiency in CAD software and engineering design tools",
            "Knowledge of spacecraft systems and technologies",
            "Strong problem-solving and analytical skills",
            "Experience with spacecraft design projects or internships"
        ],
        "Industry Type": "Aerospace, Space Exploration, Engineering"
    },
    "Space Musician": {
        "Summary": "Creates music inspired by space exploration, cosmic themes, and the wonders of the universe.",
        "Responsibilities": [
            "Composing and producing space-themed music",
            "Collaborating with scientists and educators to integrate music into space outreach and education programs",
            "Performing space music at concerts, festivals, and events",
            "Recording and releasing albums or singles inspired by space exploration"
        ],
        "Qualifications": [
            "Bachelor's degree in music composition, music production, or related field",
            "Strong musical talent and creativity",
            "Interest in space science and astronomy",
            "Ability to collaborate with scientists and educators",
            "Experience in music production and performance"
        ],
        "Industry Type": "Music, Entertainment, Science Communication"
    },
    "Astrobiologist": {
        "Summary": "Studies the origins, evolution, and distribution of life in the universe, including its potential for existing beyond Earth.",
        "Responsibilities": [
            "Conducting research on extreme environments on Earth and their relevance to extraterrestrial life",
            "Investigating the habitability of other planets and moons",
            "Searching for signs of life in space, such as microbial fossils or biosignatures",
            "Analyzing data from space missions and telescopes to identify potentially habitable worlds",
            "Collaborating with scientists from multiple disciplines to advance astrobiology"
        ],
        "Qualifications": [
            "Bachelor's, master's, or doctoral degree in astrobiology, biology, astronomy, or related field",
            "Strong research skills and scientific curiosity",
            "Knowledge of planetary science, biology, chemistry, and geology",
            "Experience with laboratory techniques and fieldwork",
            "Ability to work collaboratively and communicate findings"
        ],
        "Industry Type": "Space Exploration, Research Institutions, Academia"
    },
    "Galactic Historian": {
        "Summary": "Studies the history of galaxies, star systems, and cosmic events to understand the origins and evolution of the universe.",
        "Responsibilities": [
            "Researching historical records, astronomical observations, and scientific literature",
            "Analyzing data from telescopes and space missions to reconstruct cosmic timelines",
            "Investigating the formation and evolution of galaxies, stars, and planetary systems",
            "Contributing to scientific publications and conferences on galactic history",
            "Collaborating with astronomers and astrophysicists to interpret observational data"
        ],
        "Qualifications": [
            "Bachelor's, master's, or doctoral degree in astronomy, astrophysics, or related field",
            "Strong research and analytical skills",
            "Knowledge of cosmology, astrophysics, and observational astronomy",
            "Experience with data analysis and computer modeling",
            "Ability to communicate complex concepts to diverse audiences"
        ],
        "Industry Type": "Astronomy, Research Institutions, Academia"
    },
    "Cosmic Philosopher": {
        "Summary": "Explores philosophical questions about the nature of the universe, existence, and our place in the cosmos.",
        "Responsibilities": [
            "Studying philosophical traditions and theories related to cosmology and metaphysics",
            "Reflecting on scientific discoveries and cosmological theories",
            "Writing essays, articles, and books on cosmic philosophy",
            "Engaging in interdisciplinary dialogue with scientists, theologians, and ethicists",
            "Teaching courses and leading discussions on cosmic philosophy"
        ],
        "Qualifications": [
            "Bachelor's, master's, or doctoral degree in philosophy, cosmology, or related field",
            "Strong critical thinking and analytical skills",
            "Knowledge of philosophical traditions and cosmological theories",
            "Ability to integrate insights from science, religion, and culture",
            "Experience in academic research and teaching"
        ],
        "Industry Type": "Philosophy, Education, Research Institutions"
    },
    "Exoplanetary Geologist": {
        "Summary": "Studies the geology and surface processes of planets and moons beyond our solar system.",
        "Responsibilities": [
            "Analyzing data from telescopes and space missions to characterize exoplanets",
            "Modeling planetary interiors, atmospheres, and surface features",
            "Investigating geological processes such as volcanism, tectonics, and erosion on exoplanets",
            "Identifying and interpreting signatures of geological activity on distant worlds",
            "Contributing to the search for habitable exoplanets and signs of life"
        ],
        "Qualifications": [
            "Bachelor's, master's, or doctoral degree in geology, planetary science, or related field",
            "Strong background in geology, earth sciences, and planetary geology",
            "Experience with remote sensing data and planetary modeling",
            "Knowledge of astrobiology and planetary habitability",
            "Ability to collaborate with astronomers, physicists, and other scientists"
        ],
        "Industry Type": "Planetary Science, Space Exploration, Research Institutions"
    },
    "Intergalactic Diplomat": {
        "Summary": "Represents Earth's interests and fosters cooperation with extraterrestrial civilizations and space-faring nations.",
        "Responsibilities": [
            "Negotiating treaties, agreements, and alliances with alien civilizations",
            "Facilitating communication and cultural exchange between Earth and other worlds",
            "Addressing disputes and conflicts in interstellar relations",
            "Promoting peaceful cooperation in space exploration and colonization",
            "Advocating for Earth's interests in intergalactic forums and organizations"
        ],
        "Qualifications": [
            "Bachelor's, master's, or doctoral degree in diplomacy, international relations, or related field",
            "Experience in diplomacy, negotiation, or international law",
            "Cross-cultural communication and language skills",
            "Knowledge of space policy, astrobiology, and interstellar travel",
            "Ability to navigate complex political and cultural landscapes"
        ],
        "Industry Type": "Diplomacy, Intergalactic Relations, Government"
    },
    "Astro-Ethnographer": {
        "Summary": "Studies the cultures, societies, and civilizations of extraterrestrial beings and their interactions with humans.",
        "Responsibilities": [
            "Conducting field research and ethnographic studies on alien worlds",
            "Documenting extraterrestrial languages, customs, and belief systems",
            "Analyzing interstellar communication and cultural exchange",
            "Collaborating with anthropologists, linguists, and xenologists",
            "Sharing findings and insights with the scientific community and the public"
        ],
        "Qualifications": [
            "Bachelor's, master's, or doctoral degree in anthropology, sociology, or related field",
            "Experience in ethnographic research and cross-cultural studies",
            "Knowledge of linguistics, cultural anthropology, and interstellar communication",
            "Ability to adapt research methods to unfamiliar environments",
            "Strong writing and presentation skills"
        ],
        "Industry Type": "Anthropology, Astrobiology, Research Institutions"
    },
    "Interstellar Photographer": {
        "Summary": "Captures images of celestial objects, cosmic phenomena, and alien landscapes in distant star systems.",
        "Responsibilities": [
            "Using telescopes and spacecraft cameras to photograph galaxies, nebulae, and exoplanets",
            "Processing and enhancing astronomical images to reveal details and colors",
            "Documenting space missions and exploratory expeditions to other worlds",
            "Contributing to scientific research and public outreach through visual storytelling",
            "Sharing images with the public through exhibitions, publications, and social media"
        ],
        "Qualifications": [
            "Bachelor's degree in photography, astronomy, or related field",
            "Experience in astrophotography and image processing",
            "Knowledge of astronomy, celestial mechanics, and space missions",
            "Proficiency in photography equipment and software",
            "Ability to communicate scientific concepts through visual media"
        ],
        "Industry Type": "Astrophotography, Astronomy, Science Communication"
    }
}
    
}
# Define the range for each rating
rating_ranges = {
    "cgpa": (1, 10),
    "historyofBacklogs": (0, 15),
    "computerLiteracy": (0, 10),
    "problemSolving": (0, 10),
    "TechnicalSkill": (0, 10),
    "ResearchSkill": (0, 10),
    "communicationSkill": (0, 10),
    "interpersonalSkill": (0, 10),
    "teamwork": (0, 10),
    "adaptability": (0, 10),
    "timeManagement": (0, 10),
    "emotionalIntelligence": (0, 10),
    "continuousLearning": (0, 10),
    "leadership": (0, 10)
}

# Function to generate synthetic data
def generate_data(num_samples):
    data = []
    for _ in range(num_samples):
        sample = {}
        # Randomly select a UG Course and Specialization
        ug_course = random.choice(list(ug_courses.keys()))
        ug_specialization = random.choice(ug_courses[ug_course])
        sample["ugCourse"] = ug_course
        sample["ugSpecialization"] = ug_specialization
        
        # Assign job role based on UG course
        chosen_job_role_name, chosen_job_role_details = random.choice(list(job_roles[ug_course].items()))
        sample["jobRole"] = chosen_job_role_name
        sample["Summary"] = chosen_job_role_details["Summary"]
        
        # Concatenate Responsibilities and Qualifications
        sample["Responsibilities"] = ", ".join(chosen_job_role_details["Responsibilities"])
        sample["Qualifications"] = ", ".join(chosen_job_role_details["Qualifications"])
        
        sample["Industry Type"] = chosen_job_role_details["Industry Type"]
        
        # Generate random ratings for each rating field
        for field, (min_val, max_val) in rating_ranges.items():
            sample[field] = round(random.uniform(min_val, max_val), 1)
        
        data.append(sample)
    return data

# Generate synthetic dataset with 100 samples
synthetic_data = generate_data(100000)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_data)

# Save the DataFrame to a CSV file
df.to_csv("cp.csv", index=False)

# Display the DataFrame
print(df)
