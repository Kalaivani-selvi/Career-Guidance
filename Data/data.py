import json
import random

# Define intents
intents = [
   {
        "tag": "chemistry_interview_1",
        "patterns": ["What skills are important for a career in chemistry?"],
        "responses": ["Skills important for a career in chemistry include analytical thinking, problem-solving, attention to detail, laboratory techniques, data analysis, and strong communication skills."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_2",
        "patterns": ["How can I showcase my laboratory experience during a chemistry job interview?"],
        "responses": ["During a chemistry job interview, showcase your laboratory experience by discussing specific techniques you've used, equipment you're familiar with, experiments you've conducted, and any research projects or publications you've been involved in."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_3",
        "patterns": ["What types of industries hire chemists?"],
        "responses": ["Chemists are hired in various industries, including pharmaceuticals, biotechnology, healthcare, environmental science, food and beverage, cosmetics, materials science, and academia."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_4",
        "patterns": ["How can I stay updated on advancements in the field of chemistry?"],
        "responses": ["Stay updated on advancements in chemistry by reading scientific journals, attending conferences and seminars, participating in professional associations and online forums, and networking with peers and experts in the field."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_5",
        "patterns": ["What are some common laboratory safety practices in chemistry?"],
        "responses": ["Common laboratory safety practices in chemistry include wearing appropriate personal protective equipment (PPE), following standard operating procedures (SOPs), labeling chemicals properly, handling hazardous materials with care, and maintaining a clean and organized workspace."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_6",
        "patterns": ["How can I demonstrate my problem-solving skills during a chemistry job interview?"],
        "responses": ["Demonstrate your problem-solving skills during a chemistry job interview by discussing challenges you've encountered in research or laboratory work, outlining the steps you took to identify and address the problem, and highlighting the outcomes or solutions you achieved."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_7",
        "patterns": ["What should I emphasize when discussing my education and qualifications for a chemistry position?"],
        "responses": ["When discussing your education and qualifications for a chemistry position, emphasize relevant coursework, laboratory experience, research projects, internships, certifications, and any specialized skills or techniques you've acquired."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_8",
        "patterns": ["How can I demonstrate my passion for chemistry during a job interview?"],
        "responses": ["Demonstrate your passion for chemistry during a job interview by discussing your interest in the subject, experiences that sparked your curiosity, contributions to the field, and commitment to continued learning and professional development."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_9",
        "patterns": ["What types of research experience are valued in the field of chemistry?"],
        "responses": ["Research experience valued in the field of chemistry includes involvement in laboratory research projects, conducting independent experiments, collaborating with faculty or industry partners, presenting findings at conferences, and publishing papers in peer-reviewed journals."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_10",
        "patterns": ["How can I effectively communicate complex scientific concepts during a job interview?"],
        "responses": ["Effectively communicate complex scientific concepts during a job interview by using clear and concise language, providing real-world examples or analogies, using visual aids if applicable, and gauging the interviewer's level of understanding to adjust your explanations accordingly."],
        "context": [""]
    },
     {
        "tag": "chemistry_interview_11",
        "patterns": ["What role does chemistry play in pharmaceutical development?"],
        "responses": ["Chemistry plays a crucial role in pharmaceutical development by synthesizing and analyzing new drugs, understanding their molecular mechanisms, optimizing formulations for efficacy and safety, and ensuring compliance with regulatory standards."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_12",
        "patterns": ["How can I demonstrate my understanding of chemical principles during a job interview?"],
        "responses": ["Demonstrate your understanding of chemical principles during a job interview by discussing fundamental concepts such as stoichiometry, thermodynamics, kinetics, spectroscopy, and organic reaction mechanisms. Provide examples of how you've applied these principles in laboratory work or research projects."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_13",
        "patterns": ["What are some key considerations for conducting chemical experiments safely?"],
        "responses": ["Key considerations for conducting chemical experiments safely include wearing appropriate personal protective equipment (PPE), working in a well-ventilated area, following established protocols and procedures, using proper handling and disposal techniques for hazardous materials, and being prepared to respond to emergencies."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_14",
        "patterns": ["How can I showcase my experience with laboratory instrumentation during a chemistry job interview?"],
        "responses": ["Showcase your experience with laboratory instrumentation during a chemistry job interview by discussing specific instruments you've used, such as spectrophotometers, chromatographs, mass spectrometers, and nuclear magnetic resonance (NMR) machines. Highlight your proficiency in operation, maintenance, troubleshooting, and data analysis."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_15",
        "patterns": ["What are some emerging trends and technologies in the field of chemistry?"],
        "responses": ["Emerging trends and technologies in the field of chemistry include green chemistry, nanotechnology, computational chemistry, biomaterials, drug delivery systems, and sustainable manufacturing processes. Stay updated on these advancements to remain competitive in the field."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_16",
        "patterns": ["How can I demonstrate my ability to work independently and as part of a team in a chemistry job?"],
        "responses": ["Demonstrate your ability to work independently and as part of a team in a chemistry job by highlighting instances where you've taken initiative, managed projects or experiments, collaborated with colleagues, and contributed to group goals or publications. Discuss your communication skills, adaptability, and willingness to share knowledge and resources."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_17",
        "patterns": ["What are some challenges faced by chemists in industry, and how can they be addressed?"],
        "responses": ["Challenges faced by chemists in industry include regulatory compliance, quality control, scalability of production processes, environmental sustainability, and rapid technological advancements. These challenges can be addressed through interdisciplinary collaboration, innovation, continuous improvement initiatives, and adherence to best practices and standards."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_18",
        "patterns": ["How can I effectively communicate scientific findings and recommendations to non-technical stakeholders?"],
        "responses": ["Effectively communicate scientific findings and recommendations to non-technical stakeholders by using clear and accessible language, avoiding jargon and technical details, providing context and real-world examples, and using visual aids or multimedia presentations to enhance understanding. Tailor your message to the audience's background and level of expertise."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_19",
        "patterns": ["What are some ethical considerations in chemical research and development?"],
        "responses": ["Ethical considerations in chemical research and development include ensuring the safety and well-being of researchers and the public, minimizing environmental impact, protecting intellectual property rights, maintaining data integrity and confidentiality, and adhering to ethical guidelines and regulations governing scientific research."],
        "context": [""]
    },
    {
        "tag": "chemistry_interview_20",
        "patterns": ["How can I demonstrate my commitment to continuous learning and professional development in the field of chemistry?"],
        "responses": ["Demonstrate your commitment to continuous learning and professional development in the field of chemistry by pursuing advanced degrees or certifications, attending workshops and seminars, participating in professional associations, publishing research papers, mentoring others, and staying informed about industry trends and best practices."],
        "context": [""]
    },
     {
        "tag": "chemistry_interview_21",
        "patterns": ["What are jobs available in chemistry major?" , "Give some chemistry oriented jobs ?"],
        "responses": ["There are lots of jobs available for chemistry major . Some of the jobs are     Analytical Chemist, Biochemist, Chemical Engineer, Environmental Chemist , Forensic Scientist , Pharmaceutical Scientist , Quality Control Chemist , Research Scientist ,Toxicologist"],
        "context": [""]
    },
    {
        "tag": "web_developer_jobs",
        "patterns": ["What are jobs available for web development oriented?" , "Give some web developer oriented jobs ?"],
        "responses": ["There are lots of jobs available for web developer . Some of the jobs are     Frontend Developer,  Backend Developer,   Full Stack Developer,   UI/UX Designer,  Web Application Developer,  E-commerce Developer,  CMS Developer"],
        "context": [""]
    },
     {
        "tag": "webdev_interview_1",
        "patterns": ["What are some essential skills for a frontend developer?"],
        "responses": ["Essential skills for a frontend developer include proficiency in HTML, CSS, JavaScript, knowledge of frontend frameworks like React or Angular, responsive design principles, version control using Git, and familiarity with browser developer tools."],
        "context": [""]
    },
    {
        "tag": "webdev_interview_2",
        "patterns": ["How can I optimize website performance and loading times?"],
        "responses": ["You can optimize website performance and loading times by minimizing HTTP requests, optimizing images and multimedia content, leveraging browser caching, enabling compression, using content delivery networks (CDNs), and reducing server response times."],
        "context": [""]
    },
    {
        "tag": "webdev_interview_3",
        "patterns": ["What strategies can I use to improve website accessibility and user experience?"],
        "responses": ["To improve website accessibility and user experience, follow WCAG guidelines, use semantic HTML markup, provide alternative text for images, ensure keyboard navigation support, maintain color contrast ratios, and conduct usability testing with diverse user groups."],
        "context": [""]
    },
    {
        "tag": "webdev_interview_4",
        "patterns": ["How do you handle cross-browser compatibility issues?"],
        "responses": ["To handle cross-browser compatibility issues, use feature detection instead of browser detection, validate code against web standards, reset CSS styles using a CSS reset or normalize.css, and test websites on multiple browsers and devices during development."],
        "context": [""]
    },
    {
        "tag": "webdev_interview_5",
        "patterns": ["What are some best practices for securing web applications?"],
        "responses": ["Best practices for securing web applications include implementing HTTPS, validating and sanitizing user inputs, using parameterized queries to prevent SQL injection attacks, implementing authentication and authorization mechanisms, and keeping software dependencies updated."],
        "context": [""]
    },
     {
        "tag": "datascience_interview_1",
        "patterns": ["What programming languages are commonly used in data science?"],
        "responses": ["Commonly used programming languages in data science include Python, R, SQL, and sometimes Java or Scala for big data processing and analysis."],
        "context": [""]
    },
    {
        "tag": "datascience_interview_2",
        "patterns": ["How do you handle missing or incomplete data in a dataset?"],
        "responses": ["To handle missing or incomplete data in a dataset, you can use techniques such as imputation (replacing missing values with statistical measures like mean or median), deletion of missing data points, or predictive modeling to estimate missing values based on other variables."],
        "context": [""]
    },
    {
        "tag": "datascience_interview_3",
        "patterns": ["What is the CRISP-DM model, and how is it used in data science projects?"],
        "responses": ["The CRISP-DM (Cross-Industry Standard Process for Data Mining) model is a widely used framework for data mining and analytics projects. It consists of six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment. Data scientists use CRISP-DM to guide the lifecycle of data science projects and ensure they meet business objectives."],
        "context": [""]
    },
    {
        "tag": "datascience_interview_4",
        "patterns": ["How do you assess the performance of a machine learning model?"],
        "responses": ["To assess the performance of a machine learning model, you can use evaluation metrics such as accuracy, precision, recall, F1 score, ROC-AUC, and mean squared error (MSE), depending on the type of problem (classification, regression, etc.). Additionally, you can use techniques like cross-validation to estimate the model's performance on unseen data."],
        "context": [""]
    },
    {
        "tag": "datascience_interview_5",
        "patterns": ["What are some common algorithms used in supervised learning?"],
        "responses": ["Common algorithms used in supervised learning include linear regression, logistic regression, decision trees, random forests, support vector machines (SVM), k-nearest neighbors (KNN), naive Bayes, and neural networks."],
        "context": [""]
    },
    {
        "tag": "webdev_interview_1",
        "patterns": ["What are some essential skills for a frontend developer?"],
        "responses": ["Essential skills for a frontend developer include proficiency in HTML, CSS, JavaScript, knowledge of frontend frameworks like React or Angular, responsive design principles, version control using Git, and familiarity with browser developer tools."],
        "context": [""]
    },
    {
        "tag": "webdev_interview_2",
        "patterns": ["How can I optimize website performance and loading times?"],
        "responses": ["You can optimize website performance and loading times by minimizing HTTP requests, optimizing images and multimedia content, leveraging browser caching, enabling compression, using content delivery networks (CDNs), and reducing server response times."],
        "context": [""]
    },
    {
        "tag": "webdev_interview_3",
        "patterns": ["What strategies can I use to improve website accessibility and user experience?"],
        "responses": ["To improve website accessibility and user experience, follow WCAG guidelines, use semantic HTML markup, provide alternative text for images, ensure keyboard navigation support, maintain color contrast ratios, and conduct usability testing with diverse user groups."],
        "context": [""]
    },
    {
        "tag": "webdev_interview_4",
        "patterns": ["How do you handle cross-browser compatibility issues?"],
        "responses": ["To handle cross-browser compatibility issues, use feature detection instead of browser detection, validate code against web standards, reset CSS styles using a CSS reset or normalize.css, and test websites on multiple browsers and devices during development."],
        "context": [""]
    },
    {
        "tag": "webdev_interview_5",
        "patterns": ["What are some best practices for securing web applications?"],
        "responses": ["Best practices for securing web applications include implementing HTTPS, validating and sanitizing user inputs, using parameterized queries to prevent SQL injection attacks, implementing authentication and authorization mechanisms, and keeping software dependencies updated."],
        "context": [""]
    },
    {
        "tag": "datascience_interview_1",
        "patterns": ["What programming languages are commonly used in data science?"],
        "responses": ["Commonly used programming languages in data science include Python, R, SQL, and sometimes Java or Scala for big data processing and analysis."],
        "context": [""]
    },
    {
        "tag": "datascience_interview_2",
        "patterns": ["How do you handle missing or incomplete data in a dataset?"],
        "responses": ["To handle missing or incomplete data in a dataset, you can use techniques such as imputation (replacing missing values with statistical measures like mean or median), deletion of missing data points, or predictive modeling to estimate missing values based on other variables."],
        "context": [""]
    },
    {
        "tag": "datascience_interview_3",
        "patterns": ["What is the CRISP-DM model, and how is it used in data science projects?"],
        "responses": ["The CRISP-DM (Cross-Industry Standard Process for Data Mining) model is a widely used framework for data mining and analytics projects. It consists of six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment. Data scientists use CRISP-DM to guide the lifecycle of data science projects and ensure they meet business objectives."],
        "context": [""]
    },
    {
        "tag": "datascience_interview_4",
        "patterns": ["How do you assess the performance of a machine learning model?"],
        "responses": ["To assess the performance of a machine learning model, you can use evaluation metrics such as accuracy, precision, recall, F1 score, ROC-AUC, and mean squared error (MSE), depending on the type of problem (classification, regression, etc.). Additionally, you can use techniques like cross-validation to estimate the model's performance on unseen data."],
        "context": [""]
    },
    {
        "tag": "datascience_interview_5",
        "patterns": ["What are some common algorithms used in supervised learning?"],
        "responses": ["Common algorithms used in supervised learning include linear regression, logistic regression, decision trees, random forests, support vector machines (SVM), k-nearest neighbors (KNN), naive Bayes, and neural networks."],
        "context": [""]
    },
    {
        "tag": "fullstack_interview_1",
        "patterns": ["What are the key differences between frontend and backend development?"],
        "responses": ["Frontend development focuses on the user interface (UI) and user experience (UX) of web applications, while backend development involves server-side logic, databases, and application architecture. Frontend developers work with HTML, CSS, JavaScript, and frontend frameworks, while backend developers use languages like Python, Ruby, Java, or Node.js, along with databases like MySQL, MongoDB, or PostgreSQL."],
        "context": [""]
    },
    {
        "tag": "fullstack_interview_2",
        "patterns": ["What is RESTful API, and why is it important in full stack development?"],
        "responses": ["RESTful API (Representational State Transfer) is an architectural style for designing networked applications. It uses standard HTTP methods like GET, POST, PUT, DELETE to perform CRUD (Create, Read, Update, Delete) operations on resources. RESTful APIs are important in full stack development for enabling communication between frontend and backend components, facilitating interoperability, and supporting scalability and maintainability of web applications."],
        "context": [""]
    },
    {
        "tag": "fullstack_interview_3",
        "patterns": ["How do you ensure data security in full stack development?"],
        "responses": ["To ensure data security in full stack development, use secure authentication and authorization mechanisms, encrypt sensitive data in transit and at rest, implement input validation and parameterized queries to prevent SQL injection attacks, sanitize user inputs, and keep software dependencies updated to patch security vulnerabilities."],
        "context": [""]
    },
    {
        "tag": "fullstack_interview_4",
        "patterns": ["What is the role of version control systems like Git in full stack development?"],
        "responses": ["Version control systems like Git play a crucial role in full stack development by enabling collaborative software development, tracking changes to codebase, facilitating code review and collaboration among team members, branching and merging"],
        "context": [""]
    },
     {
        "tag": "data_analysis_interview_1",
        "patterns": ["What are the key steps in the data analysis process?"],
        "responses": ["The key steps in the data analysis process include defining the problem statement, collecting and cleaning data, exploring and visualizing data, performing statistical analysis, building predictive models, interpreting results, and communicating findings to stakeholders."],
        "context": [""]
    },
    {
        "tag": "data_analysis_interview_2",
        "patterns": ["How do you handle missing or outlier data in a dataset?"],
        "responses": ["To handle missing or outlier data in a dataset, you can use techniques such as imputation, removal of outliers, data transformation (e.g., logarithmic transformation), or treating missing values as a separate category, depending on the nature of the data and the analysis goals."],
        "context": [""]
    },
    {
        "tag": "data_analysis_interview_3",
        "patterns": ["What data visualization tools and techniques do you use for exploratory data analysis?"],
        "responses": ["For exploratory data analysis, I use data visualization tools like Matplotlib, Seaborn, Plotly, and Tableau to create charts, graphs, histograms, and heatmaps. I also use techniques such as scatter plots, box plots, bar charts, and correlation matrices to explore relationships and patterns in the data."],
        "context": [""]
    },
    {
        "tag": "machine_learning_interview_1",
        "patterns": ["What are some common algorithms used in machine learning?"],
        "responses": ["Common algorithms used in machine learning include linear regression, logistic regression, decision trees, random forests, support vector machines (SVM), k-nearest neighbors (KNN), naive Bayes, neural networks, and clustering algorithms like K-means and hierarchical clustering."],
        "context": [""]
    },
    {
        "tag": "machine_learning_interview_2",
        "patterns": ["How do you evaluate the performance of a machine learning model?"],
        "responses": ["To evaluate the performance of a machine learning model, you can use metrics such as accuracy, precision, recall, F1 score, ROC-AUC, mean squared error (MSE), and R-squared, depending on the type of problem (classification, regression, etc.). Additionally, you can use techniques like cross-validation to estimate the model's performance on unseen data."],
        "context": [""]
    },
    {
        "tag": "machine_learning_interview_3",
        "patterns": ["What are some challenges you may encounter when working with real-world data?"],
        "responses": ["Challenges when working with real-world data include data quality issues, missing or incomplete data, data privacy and security concerns, unbalanced datasets, noisy data, feature engineering complexities, overfitting, and scalability issues with large datasets."],
        "context": [""]
    },
    {
        "tag": "data_engineering_interview_1",
        "patterns": ["What are some key components of a data pipeline?"],
        "responses": ["Key components of a data pipeline include data ingestion (extracting data from various sources), data preprocessing (cleaning, transforming, and enriching data), data storage (structured or unstructured storage solutions), data processing (batch or real-time processing), data analysis (performing queries or analytics), and data visualization (presenting insights to end-users)."],
        "context": [""]
    },
    {
        "tag": "data_engineering_interview_2",
        "patterns": ["How do you ensure data quality and integrity in a data pipeline?"],
        "responses": ["To ensure data quality and integrity in a data pipeline, I implement data validation checks, enforce data governance policies, perform data profiling and cleansing, establish data lineage and metadata management, monitor data pipelines for anomalies or errors, and implement error handling and logging mechanisms."],
        "context": [""]
    },
    {
        "tag": "data_engineering_interview_3",
        "patterns": ["What is the role of ETL (Extract, Transform, Load) in data engineering?"],
        "responses": ["ETL (Extract, Transform, Load) is a process used in data engineering to extract data from various sources, transform it into a consistent format suitable for analysis or storage, and load it into a destination like a data warehouse or database. ETL helps integrate disparate data sources, standardize data formats, and prepare data for analysis or reporting purposes."],
        "context": [""]
    },
    {
        "tag": "business_intelligence_interview_1",
        "patterns": ["What is the role of business intelligence in decision-making?"],
        "responses": ["Business intelligence (BI) plays a crucial role in decision-making by providing insights and actionable information derived from data analysis. BI tools and dashboards enable stakeholders to monitor key performance indicators (KPIs), track business metrics, identify trends and patterns, and make data-driven decisions to drive business growth and performance."],
        "context": [""]
    },
    {
        "tag": "business_intelligence_interview_2",
        "patterns": ["How do you design effective data visualizations for business users?"],
        "responses": ["To design effective data visualizations for business users, I focus on simplicity, clarity, and relevance. I choose appropriate chart types (e.g., bar charts, line charts, pie charts) based on the data and the message I want to convey. I use color, size, and labels judiciously to highlight key insights and trends, and I ensure that the visualization is intuitive and easy to interpret."],
        "context": [""]
    },
    {
        "tag": "business_intelligence_interview_3",
        "patterns": ["What are some common challenges in implementing a business intelligence solution?"],
        "responses": ["Common challenges in implementing a business intelligence solution include data silos and integration issues, data quality and consistency problems, lack of user adoption and training, scalability and performance concerns, security and compliance requirements, and aligning BI initiatives with business goals and priorities."],
        "context": [""]
    },
    {
        "tag": "statistics_interview_1",
        "patterns": ["What statistical techniques do you use for hypothesis testing?"],
        "responses": ["For hypothesis testing, I use techniques such as t-tests (for comparing means), ANOVA (for comparing means of multiple groups), chi-square tests (for categorical data), correlation analysis (for measuring relationships between variables), regression analysis (for predicting outcomes), and non-parametric tests (for data that doesn't meet assumptions of parametric tests)."],
        "context": [""]
    },
    {
        "tag": "statistics_interview_2",
        "patterns": ["How do you select the appropriate statistical model for your data analysis?"],
        "responses": ["To select the appropriate statistical model for data analysis, I consider factors such as the type of data (continuous, categorical, etc.), the distribution of data, the research question or hypothesis, the assumptions of the statistical model, and the desired level of precision and accuracy. I also perform exploratory data analysis (EDA) to understand the characteristics and relationships within the data before choosing a statistical model."],
        "context": [""]
    },
    {
        "tag": "statistics_interview_3",
        "patterns": ["What is the difference between descriptive and inferential statistics?"],
        "responses": ["Descriptive statistics are used to summarize and describe the main features of a dataset, such as central tendency (mean, median, mode), dispersion (range, variance, standard deviation), and distribution (normality, skewness, kurtosis). Inferential statistics, on the other hand, are used to draw conclusions or make inferences about a population based on a sample from that population. Inferential statistics include hypothesis testing, confidence intervals, and regression analysis."],
        "context": [""]
    },
    {
        "tag": "research_science_interview_1",
        "patterns": ["What is the importance of reproducibility in scientific research?"],
        "responses": ["Reproducibility is crucial in scientific research because it ensures the reliability and validity of research findings. Reproducible research allows other scientists to verify and build upon previous findings, enhances the credibility of scientific knowledge, promotes transparency and accountability, and helps identify errors or biases in experimental methods or data analysis."],
        "context": [""]
    },
    {
        "tag": "research_science_interview_2",
        "patterns": ["How do you design experiments to test scientific hypotheses?"],
        "responses": ["To design experiments to test scientific hypotheses, I define clear research questions or hypotheses, identify variables and controls, select appropriate experimental methods and procedures, ensure randomization and replication, minimize bias and confounding factors, and establish criteria for data collection and analysis. I also consider ethical considerations and potential risks associated with the experiment."],
        "context": [""]
    },
    {
        "tag": "research_science_interview_3",
        "patterns": ["What are some key ethical considerations in scientific research?"],
        "responses": ["Key ethical considerations in scientific research include obtaining informed consent from participants, ensuring confidentiality and privacy of research data, minimizing risks and potential harm to participants, disclosing conflicts of interest, adhering to ethical guidelines and regulations governing research conduct, and reporting research findings accurately and transparently."],
        "context": [""]
    },
    {
        "tag": "frontend_interview_1",
        "patterns": ["What are the key features of HTML5?"],
        "responses": ["HTML5 introduces new elements like <header>, <footer>, <section>, <article>, <nav>, <video>, <audio>, <canvas> for better structure and multimedia support. It also supports advanced CSS3 features, local storage, geolocation APIs, and enhanced form input types."],
        "context": [""]
    },
    {
        "tag": "frontend_interview_2",
        "patterns": ["What are some benefits of using CSS pre-processors like Sass or Less?"],
        "responses": ["CSS pre-processors like Sass or Less offer benefits such as variables for reusability and easier maintenance, nesting for hierarchical styling, mixins for code reuse, and functions for dynamic styles. They also support modularization and organization of CSS code, resulting in cleaner and more maintainable stylesheets."],
        "context": [""]
    },
    {
        "tag": "frontend_interview_3",
        "patterns": ["What are some common techniques for optimizing website performance?"],
        "responses": ["Common techniques for optimizing website performance include minimizing HTTP requests, reducing file sizes (e.g., compressing images, minifying CSS and JavaScript), leveraging browser caching, using content delivery networks (CDNs), implementing lazy loading for images and content, and reducing server response times."],
        "context": [""]
    },
    {
        "tag": "backend_interview_1",
        "patterns": ["What is the role of a web server in backend development?"],
        "responses": ["In backend development, a web server is responsible for handling incoming requests from clients (e.g., web browsers), processing those requests, and sending back appropriate responses. It manages routing, request processing, authentication, authorization, and interacts with databases or other services to fulfill client requests."],
        "context": [""]
    },
    {
        "tag": "backend_interview_2",
        "patterns": ["What are some common databases used in backend development?"],
        "responses": ["Common databases used in backend development include relational databases like MySQL, PostgreSQL, Oracle, and SQL Server, as well as NoSQL databases like MongoDB, Cassandra, Couchbase, and Redis. The choice of database depends on factors like data structure, scalability, performance, and consistency requirements."],
        "context": [""]
    },
    {
        "tag": "backend_interview_3",
        "patterns": ["What is the difference between synchronous and asynchronous programming in backend development?"],
        "responses": ["Synchronous programming executes tasks sequentially, where each task waits for the previous one to complete before starting. Asynchronous programming allows tasks to execute independently of one another, enabling non-blocking operations and better utilization of resources. Asynchronous programming is commonly used in backend development for handling I/O-bound operations and improving performance."],
        "context": [""]
    },
    {
        "tag": "fullstack_interview_1",
        "patterns": ["What are the advantages of being a full stack developer?"],
        "responses": ["Advantages of being a full stack developer include having a broader skill set and understanding of both frontend and backend technologies, being able to work on end-to-end development projects, faster development cycles, better collaboration with frontend and backend teams, and the ability to troubleshoot and debug across the entire stack."],
        "context": [""]
    },
    {
        "tag": "fullstack_interview_2",
        "patterns": ["How do you ensure security in full stack development?"],
        "responses": ["In full stack development, security measures include implementing secure authentication and authorization mechanisms, input validation and parameterized queries to prevent SQL injection attacks, encryption of sensitive data, using HTTPS for secure communication, adhering to least privilege principles, and keeping software dependencies updated to patch security vulnerabilities."],
        "context": [""]
    },
    {
        "tag": "fullstack_interview_3",
        "patterns": ["What role does version control play in full stack development?"],
        "responses": ["Version control systems like Git play a crucial role in full stack development by enabling collaborative software development, tracking changes to codebase, facilitating code review and collaboration among team members, branching and merging code changes, and ensuring version history and accountability."],
        "context": [""]
    },
     {
        "tag": "software_engineering_interview_1",
        "patterns": ["What are some principles of object-oriented programming (OOP)?"],
        "responses": ["Principles of object-oriented programming (OOP) include encapsulation (data hiding), inheritance (reuse of code and behavior), polymorphism (multiple forms of a function or method), and abstraction (representation of essential features while hiding implementation details). OOP promotes modular, reusable, and maintainable software design."],
        "context": [""]
    },
    {
        "tag": "software_engineering_interview_2",
        "patterns": ["What is the difference between functional programming and object-oriented programming?"],
        "responses": ["Functional programming emphasizes the use of pure functions and immutable data, avoids side effects and mutable state, and focuses on higher-order functions, recursion, and function composition. Object-oriented programming, on the other hand, focuses on objects and classes, encapsulation, inheritance, and polymorphism, and uses stateful objects and methods for computation."],
        "context": [""]
    },
    {
        "tag": "software_engineering_interview_3",
        "patterns": ["How do you ensure code quality and maintainability in software development?"],
        "responses": ["To ensure code quality and maintainability, I follow best practices such as writing clean and readable code, adhering to coding standards and conventions, using meaningful variable and function names, documenting code and its functionality, performing code reviews and unit testing, refactoring code to remove duplication and improve clarity, and modularizing code into reusable components."],
        "context": [""]
    },
     {
        "tag": "web_application_interview_1",
        "patterns": ["What are some common security vulnerabilities in web applications?"],
        "responses": ["Common security vulnerabilities in web applications include SQL injection, cross-site scripting (XSS), cross-site request forgery (CSRF), insecure direct object references, broken authentication and session management, security misconfigurations, sensitive data exposure, and lack of input validation and sanitization."],
        "context": [""]
    },
    {
        "tag": "web_application_interview_2",
        "patterns": ["What are the advantages of using frameworks like React, Angular, or Vue.js for web development?"],
        "responses": ["Frameworks like React, Angular, and Vue.js offer advantages such as component-based architecture for reusability and modularity, virtual DOM for efficient rendering and performance optimization, declarative syntax for describing UI components and their behavior, and ecosystem support for state management, routing, and testing."],
        "context": [""]
    },
    {
        "tag": "web_application_interview_3",
        "patterns": ["How do you handle client-side and server-side validation in web forms?"],
        "responses": ["Client-side validation is performed using JavaScript to validate form inputs in the user's browser before submitting the form to the server. Server-side validation is performed on the server to validate form inputs and ensure data integrity and security. Both client-side and server-side validation are important to provide a seamless and secure user experience."],
        "context": [""]
    },
     {
        "tag": "systems_architecture_interview_1",
        "patterns": ["What are some key considerations in designing scalable systems architecture?"],
        "responses": ["Key considerations in designing scalable systems architecture include horizontal and vertical scalability, load balancing and auto-scaling, distributed computing and microservices architecture, fault tolerance and redundancy, caching strategies, data partitioning and sharding, and performance monitoring and optimization."],
        "context": [""]
    },
    {
        "tag": "systems_architecture_interview_2",
        "patterns": ["What are the differences between monolithic and microservices architectures?"],
        "responses": ["In a monolithic architecture, the entire application is built as a single unit, with all components tightly coupled and deployed together. In a microservices architecture, the application is broken down into smaller, independent services that are loosely coupled and can be developed, deployed, and scaled independently. Microservices promote modularity, flexibility, and scalability but introduce complexities in deployment, monitoring, and coordination."],
        "context": [""]
    },
    {
        "tag": "systems_architecture_interview_3",
        "patterns": ["How do you ensure high availability and reliability in systems architecture?"],
        "responses": ["To ensure high availability and reliability, I design systems with redundancy and failover mechanisms, implement load balancing and traffic distribution, use distributed and replicated data storage solutions, employ monitoring and alerting systems for proactive detection of failures, and conduct regular testing and disaster recovery drills."],
        "context": [""]
    },
    {
        "tag": "devops_interview_1",
        "patterns": ["What is the role of DevOps in software development and deployment?"],
        "responses": ["DevOps is a culture, philosophy, and set of practices that promotes collaboration and integration between software development (Dev) and IT operations (Ops) teams. DevOps aims to automate and streamline the software delivery pipeline, improve deployment frequency, achieve faster time-to-market, and enhance overall software quality and reliability."],
        "context": [""]
    },
    {
        "tag": "devops_interview_2",
        "patterns": ["What are some key components of a CI/CD pipeline?"],
        "responses": ["Key components of a CI/CD (Continuous Integration/Continuous Deployment) pipeline include version control systems (e.g., Git), build automation tools (e.g., Jenkins, Travis CI), automated testing frameworks (e.g., JUnit, Selenium), artifact repositories (e.g., Nexus, Artifactory), deployment automation tools (e.g., Ansible, Puppet), and monitoring and logging solutions (e.g., ELK stack, Prometheus)."],
        "context": [""]
    },
    {
        "tag": "devops_interview_3",
        "patterns": ["How do you ensure security in a CI/CD pipeline?"],
        "responses": ["To ensure security in a CI/CD pipeline, I implement security controls such as code scanning and static analysis for vulnerabilities, dependency scanning to detect outdated or vulnerable dependencies, secrets management for secure storage and retrieval of credentials, and automated security testing (e.g., penetration testing, vulnerability scanning) as part of the CI/CD workflow."],
        "context": [""]
    }

]

# Generate synthetic data
synthetic_data = []

# Number of samples per intent
num_samples_per_intent = 40

for intent in intents:
    for _ in range(num_samples_per_intent):
        pattern = random.choice(intent["patterns"])
        response = random.choice(intent["responses"])
        synthetic_data.append({
            "tag": intent["tag"],
            "patterns": [pattern],
            "responses": [response],
            "context": intent["context"]
        })

# Save synthetic data to JSON file
with open("synthetic_data.json", "w") as file:
    json.dump(synthetic_data, file, indent=4)

print("Synthetic data generated and saved successfully.")
