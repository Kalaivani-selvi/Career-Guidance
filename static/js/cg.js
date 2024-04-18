

function updateUGSpecializations() {
    const ugCourse = document.getElementById('ugCourse').value;
    const ugSpecializationSelect = document.getElementById('ugSpecialization');

    // Clear previous options
    ugSpecializationSelect.innerHTML = '';

    // Add relevant specializations based on the selected UG course
    switch (ugCourse) {
        case 'BSc':
            ugSpecializationSelect.options.add(new Option('Physics', 'physics'));
            ugSpecializationSelect.options.add(new Option('Chemistry', 'chemistry'));
            ugSpecializationSelect.options.add(new Option('Biology', 'biology'));
            ugSpecializationSelect.options.add(new Option('Mathematics', 'mathematics'));
            ugSpecializationSelect.options.add(new Option('Computer Science', 'computer-science'));
            ugSpecializationSelect.options.add(new Option('Environmental Science', 'environmental-science'));
            ugSpecializationSelect.options.add(new Option('Statistics', 'statistics'));
            ugSpecializationSelect.options.add(new Option('Geology', 'geology'));
            ugSpecializationSelect.options.add(new Option('Astrophysics', 'astrophysics'));
            ugSpecializationSelect.options.add(new Option('Data Science', 'data-science'));
            ugSpecializationSelect.options.add(new Option('Biochemistry', 'biochemistry'));
            ugSpecializationSelect.options.add(new Option('Microbiology', 'microbiology'));
            ugSpecializationSelect.options.add(new Option('Neuroscience', 'neuroscience'));
            ugSpecializationSelect.options.add(new Option('Biophysics', 'biophysics'));
            ugSpecializationSelect.options.add(new Option('Applied Mathematics', 'applied-mathematics'));
            ugSpecializationSelect.options.add(new Option('Genetics', 'genetics'));
            ugSpecializationSelect.options.add(new Option('Biotechnology', 'biotechnology'));
            ugSpecializationSelect.options.add(new Option('Marine Biology', 'marine-biology'));
            ugSpecializationSelect.options.add(new Option('Zoology', 'zoology'));
            // Add more specializations as needed
            break;
        case 'BA':
            ugSpecializationSelect.options.add(new Option('Literature', 'literature'));
            ugSpecializationSelect.options.add(new Option('History', 'history'));
            ugSpecializationSelect.options.add(new Option('Philosophy', 'philosophy'));
            ugSpecializationSelect.options.add(new Option('Sociology', 'sociology'));
            ugSpecializationSelect.options.add(new Option('Psychology', 'psychology'));
            ugSpecializationSelect.options.add(new Option('Anthropology', 'anthropology'));
            ugSpecializationSelect.options.add(new Option('Political Science', 'political-science'));
            ugSpecializationSelect.options.add(new Option('Economics', 'economics'));
            ugSpecializationSelect.options.add(new Option('Linguistics Cultural Studies', 'linguistics-cultural-studies'));
            ugSpecializationSelect.options.add(new Option('Fine Arts', 'fine-arts'));
            ugSpecializationSelect.options.add(new Option('Drama and Theater', 'drama-theater'));
            ugSpecializationSelect.options.add(new Option('Visual Art', 'visual-art'));
            ugSpecializationSelect.options.add(new Option('Music', 'music'));
            ugSpecializationSelect.options.add(new Option('Communication Studies', 'communication-studies'));
            ugSpecializationSelect.options.add(new Option('Gender Studies', 'gender-studies'));
            ugSpecializationSelect.options.add(new Option('International Relations', 'international-relations'));
            ugSpecializationSelect.options.add(new Option('Religious Studies', 'religious-studies'));
            ugSpecializationSelect.options.add(new Option('Media Studies', 'media-studies'));
            // Add more specializations as needed
            break;
        case 'BCom':
            ugSpecializationSelect.options.add(new Option('Accounting', 'accounting'));
            ugSpecializationSelect.options.add(new Option('Finance', 'finance'));
            ugSpecializationSelect.options.add(new Option('Marketing', 'marketing'));
            ugSpecializationSelect.options.add(new Option('Management', 'management'));
            ugSpecializationSelect.options.add(new Option('Economics', 'economics'));
            ugSpecializationSelect.options.add(new Option('International Business', 'international-business'));
            ugSpecializationSelect.options.add(new Option('Entrepreneurship', 'entrepreneurship'));
            ugSpecializationSelect.options.add(new Option('Business Analytics', 'business-analytics'));
            ugSpecializationSelect.options.add(new Option('Supply Chain Management', 'supply-chain-management'));
            ugSpecializationSelect.options.add(new Option('Human Resource Management', 'human-resource-management'));
            ugSpecializationSelect.options.add(new Option('Retail Management', 'retail-management'));
            ugSpecializationSelect.options.add(new Option('E-commerce', 'e-commerce'));
            ugSpecializationSelect.options.add(new Option('Hospitality Management', 'hospitality-management'));
            ugSpecializationSelect.options.add(new Option('Strategic Management', 'strategic-management'));
            ugSpecializationSelect.options.add(new Option('Operations Management', 'operations-management'));
            ugSpecializationSelect.options.add(new Option('Banking and Finance', 'banking-and-finance'));
            ugSpecializationSelect.options.add(new Option('Corporate Law', 'corporate-law'));
            // Add more specializations as needed
            break;
        case 'BE or BTech':
            ugSpecializationSelect.options.add(new Option('Electrical Engineering', 'electrical'));
            ugSpecializationSelect.options.add(new Option('Mechanical Engineering', 'mechanical'));
            ugSpecializationSelect.options.add(new Option('Civil Engineering', 'civil'));
            ugSpecializationSelect.options.add(new Option('Computer Science and Engineering', 'computer-science'));
            ugSpecializationSelect.options.add(new Option('Chemical Engineering', 'chemical'));
            ugSpecializationSelect.options.add(new Option('Aerospace Engineering', 'aerospace'));
            ugSpecializationSelect.options.add(new Option('Biomedical Engineering', 'biomedical'));
            ugSpecializationSelect.options.add(new Option('Environmental Engineering', 'environmental'));
            ugSpecializationSelect.options.add(new Option('Materials Science and Engineering', 'materials-science'));
            ugSpecializationSelect.options.add(new Option('Petroleum Engineering', 'petroleum'));
            ugSpecializationSelect.options.add(new Option('Mechatronics Engineering', 'mechatronics'));
            ugSpecializationSelect.options.add(new Option('Information Technology', 'information-technology'));
            ugSpecializationSelect.options.add(new Option('Telecommunication Engineering', 'telecommunication'));
            ugSpecializationSelect.options.add(new Option('Automobile Engineering', 'automobile'));
            ugSpecializationSelect.options.add(new Option('Robotics Engineering', 'robotics'));
            ugSpecializationSelect.options.add(new Option('Nanotechnology', 'nanotechnology'));
            ugSpecializationSelect.options.add(new Option('Biotechnology', 'biotechnology'));
            ugSpecializationSelect.options.add(new Option('Computer Network Engineering', 'computer-network'));
            ugSpecializationSelect.options.add(new Option('Software Engineering', 'software'));
            ugSpecializationSelect.options.add(new Option('Cybersecurity', 'cybersecurity'));
            ugSpecializationSelect.options.add(new Option('Data Science', 'data-science'));
            ugSpecializationSelect.options.add(new Option('Renewable Energy Engineering', 'renewable-energy'));
            ugSpecializationSelect.options.add(new Option('Wireless Communication Engineering', 'wireless-communication'));
            ugSpecializationSelect.options.add(new Option('Control Systems Engineering', 'control-systems'));
            ugSpecializationSelect.options.add(new Option('Structural Engineering', 'structural'));
            ugSpecializationSelect.options.add(new Option('Geotechnical Engineering', 'geotechnical'));
            ugSpecializationSelect.options.add(new Option('Power Systems Engineering', 'power-systems'));
            ugSpecializationSelect.options.add(new Option('Digital Electronics Engineering', 'digital-electronics'));
            // Add more specializations as needed
            break;
        case 'BFA':
            ugSpecializationSelect.options.add(new Option('Visual Arts', 'visual-arts'));
            ugSpecializationSelect.options.add(new Option('Performing Arts', 'performing-arts'));
            ugSpecializationSelect.options.add(new Option('Creative Writing', 'creative-writing'));
            ugSpecializationSelect.options.add(new Option('Film and Television Production', 'film-television-production'));
            ugSpecializationSelect.options.add(new Option('Dance', 'dance'));
            ugSpecializationSelect.options.add(new Option('Music', 'music'));
            ugSpecializationSelect.options.add(new Option('Photography', 'photography'));
            ugSpecializationSelect.options.add(new Option('Graphic Design', 'graphic-design'));
            ugSpecializationSelect.options.add(new Option('Sculpture', 'sculpture'));
            ugSpecializationSelect.options.add(new Option('Illustration', 'illustration'));
            ugSpecializationSelect.options.add(new Option('Animation', 'animation'));
            ugSpecializationSelect.options.add(new Option('Art History', 'art-history'));
            ugSpecializationSelect.options.add(new Option('Costume Design', 'costume-design'));
            ugSpecializationSelect.options.add(new Option('Digital Arts', 'digital-arts'));
            ugSpecializationSelect.options.add(new Option('Printmaking', 'printmaking'));
            ugSpecializationSelect.options.add(new Option('Ceramics', 'ceramics'));
            ugSpecializationSelect.options.add(new Option('Art Education', 'art-education'));
            ugSpecializationSelect.options.add(new Option('Theater Design', 'theater-design'));
            ugSpecializationSelect.options.add(new Option('Art Therapy', 'art-therapy'));
            // Add more specializations as needed
            break;
        case 'BBA':
            ugSpecializationSelect.options.add(new Option('Human Resource Management', 'hr-management'));
            ugSpecializationSelect.options.add(new Option('Finance', 'finance'));
            ugSpecializationSelect.options.add(new Option('Marketing', 'marketing'));
            ugSpecializationSelect.options.add(new Option('International Business', 'international-business'));
            ugSpecializationSelect.options.add(new Option('Entrepreneurship', 'entrepreneurship'));
            ugSpecializationSelect.options.add(new Option('Supply Chain Management', 'supply-chain-management'));
            ugSpecializationSelect.options.add(new Option('Business Analytics', 'business-analytics'));
            ugSpecializationSelect.options.add(new Option('Operations Management', 'operations-management'));
            ugSpecializationSelect.options.add(new Option('Strategic Management', 'strategic-management'));
            ugSpecializationSelect.options.add(new Option('E-commerce', 'e-commerce'));
            ugSpecializationSelect.options.add(new Option('Corporate Finance', 'corporate-finance'));
            ugSpecializationSelect.options.add(new Option('Organizational Behavior', 'organizational-behavior'));
            ugSpecializationSelect.options.add(new Option('Business Ethics', 'business-ethics'));
            ugSpecializationSelect.options.add(new Option('Management Information Systems', 'management-information-systems'));
            ugSpecializationSelect.options.add(new Option('Project Management', 'project-management'));
            ugSpecializationSelect.options.add(new Option('Leadership', 'leadership'));
            ugSpecializationSelect.options.add(new Option('Business Law', 'business-law'));
            ugSpecializationSelect.options.add(new Option('Customer Relationship Management', 'customer-relationship-management'));
            ugSpecializationSelect.options.add(new Option('Retail Management', 'retail-management'));
            ugSpecializationSelect.options.add(new Option('Sports Management', 'sports-management'));
            // Add more specializations as needed
            break;
        case 'BArch':
            ugSpecializationSelect.options.add(new Option('Architectural Design', 'architectural-design'));
            ugSpecializationSelect.options.add(new Option('Urban Planning', 'urban-planning'));
            ugSpecializationSelect.options.add(new Option('Landscape Architecture', 'landscape-architecture'));
            ugSpecializationSelect.options.add(new Option('Sustainable Architecture', 'sustainable-architecture'));
            ugSpecializationSelect.options.add(new Option('Interior Design', 'interior-design'));
            ugSpecializationSelect.options.add(new Option('Historic Preservation', 'historic-preservation'));
            ugSpecializationSelect.options.add(new Option('Building Technology', 'building-technology'));
            ugSpecializationSelect.options.add(new Option('Architectural History', 'architectural-history'));
            ugSpecializationSelect.options.add(new Option('Construction Management', 'construction-management'));
            ugSpecializationSelect.options.add(new Option('Real Estate Development', 'real-estate-development'));
            ugSpecializationSelect.options.add(new Option('Digital Architecture', 'digital-architecture'));
            ugSpecializationSelect.options.add(new Option('Architectural Theory', 'architectural-theory'));
            ugSpecializationSelect.options.add(new Option('Environmental Design', 'environmental-design'));
            ugSpecializationSelect.options.add(new Option('Community Planning', 'community-planning'));
            ugSpecializationSelect.options.add(new Option('Architectural Education', 'architectural-education'));
            ugSpecializationSelect.options.add(new Option('Healthcare Architecture', 'healthcare-architecture'));
            ugSpecializationSelect.options.add(new Option('Lighting Design', 'lighting-design'));
            ugSpecializationSelect.options.add(new Option('Acoustic Design', 'acoustic-design'));
            ugSpecializationSelect.options.add(new Option('Architectural Visualization', 'architectural-visualization'));
            // Add more specializations as needed
            break;
        case 'BCA':
            ugSpecializationSelect.options.add(new Option('Software Development', 'software-development'));
            ugSpecializationSelect.options.add(new Option('Database Management', 'database-management'));
            ugSpecializationSelect.options.add(new Option('Web Development', 'web-development'));
            ugSpecializationSelect.options.add(new Option('Mobile App Development', 'mobile-app-development'));
            ugSpecializationSelect.options.add(new Option('Network Administration', 'network-administration'));
            ugSpecializationSelect.options.add(new Option('Information Security', 'information-security'));
            ugSpecializationSelect.options.add(new Option('Artificial Intelligence', 'artificial-intelligence'));
            ugSpecializationSelect.options.add(new Option('Data Science', 'data-science'));
            ugSpecializationSelect.options.add(new Option('Cloud Computing', 'cloud-computing'));
            ugSpecializationSelect.options.add(new Option('Game Development', 'game-development'));
            ugSpecializationSelect.options.add(new Option('Human-Computer Interaction', 'human-computer-interaction'));
            ugSpecializationSelect.options.add(new Option('Computer Graphics', 'computer-graphics'));
            ugSpecializationSelect.options.add(new Option('Software Testing', 'software-testing'));
            ugSpecializationSelect.options.add(new Option('E-commerce Development', 'e-commerce-development'));
            ugSpecializationSelect.options.add(new Option('IT Consulting', 'it-consulting'));
            ugSpecializationSelect.options.add(new Option('Database Administration', 'database-administration'));
            ugSpecializationSelect.options.add(new Option('Cybersecurity', 'cybersecurity'));
            ugSpecializationSelect.options.add(new Option('Business Intelligence', 'business-intelligence'));
            ugSpecializationSelect.options.add(new Option('Computer Forensics', 'computer-forensics'));
            // Add more specializations as needed
            break;
        case 'BEd':
            ugSpecializationSelect.options.add(new Option('Elementary Education', 'elementary-education'));
            ugSpecializationSelect.options.add(new Option('Secondary Education', 'secondary-education'));
            ugSpecializationSelect.options.add(new Option('Special Education', 'special-education'));
            ugSpecializationSelect.options.add(new Option('Early Childhood Education', 'early-childhood-education'));
            ugSpecializationSelect.options.add(new Option('Physical Education', 'physical-education'));
            ugSpecializationSelect.options.add(new Option('Mathematics Education', 'mathematics-education'));
            ugSpecializationSelect.options.add(new Option('Science Education', 'science-education'));
            ugSpecializationSelect.options.add(new Option('English Education', 'english-education'));
            ugSpecializationSelect.options.add(new Option('Social Studies Education', 'social-studies-education'));
            ugSpecializationSelect.options.add(new Option('Art Education', 'art-education'));
            ugSpecializationSelect.options.add(new Option('Music Education', 'music-education'));
            ugSpecializationSelect.options.add(new Option('Educational Leadership', 'educational-leadership'));
            ugSpecializationSelect.options.add(new Option('Curriculum and Instruction', 'curriculum-instruction'));
            ugSpecializationSelect.options.add(new Option('Technology Education', 'technology-education'));
            ugSpecializationSelect.options.add(new Option('Special Needs Education', 'special-needs-education'));
            ugSpecializationSelect.options.add(new Option('TESOL', 'tesol'));
            ugSpecializationSelect.options.add(new Option('Guidance and Counseling', 'guidance-counseling'));
            ugSpecializationSelect.options.add(new Option('Adult Education', 'adult-education'));
            ugSpecializationSelect.options.add(new Option('Educational Psychology', 'educational-psychology'));
            ugSpecializationSelect.options.add(new Option('International Education', 'international-education'));
            // Add more specializations as needed
            break;
        case 'BSA':
            ugSpecializationSelect.options.add(new Option('Astro-Painting', 'astro-painting'));
            ugSpecializationSelect.options.add(new Option('Galactic Sculpture', 'galactic-sculpture'));
            ugSpecializationSelect.options.add(new Option('Celestial Photography', 'celestial-photography'));
            ugSpecializationSelect.options.add(new Option('Space Literature', 'space-literature'));
            ugSpecializationSelect.options.add(new Option('Astronomical Music Composition', 'astronomical-music-composition'));
            ugSpecializationSelect.options.add(new Option('Exoplanetary Architecture', 'exoplanetary-architecture'));
            ugSpecializationSelect.options.add(new Option('Astrobiology Illustration', 'astrobiology-illustration'));
            ugSpecializationSelect.options.add(new Option('Interstellar Dance', 'interstellar-dance'));
            ugSpecializationSelect.options.add(new Option('Cosmic Fashion Design', 'cosmic-fashion-design'));
            ugSpecializationSelect.options.add(new Option('Planetary Poetry', 'planetary-poetry'));
            ugSpecializationSelect.options.add(new Option('Space Philosophy', 'space-philosophy'));
            ugSpecializationSelect.options.add(new Option('Astro-Graphic Design', 'astro-graphic-design'));
            ugSpecializationSelect.options.add(new Option('Lunar Landscape Painting', 'lunar-landscape-painting'));
            ugSpecializationSelect.options.add(new Option('Martian Sculpture', 'martian-sculpture'));
            ugSpecializationSelect.options.add(new Option('Saturnian Installation Art', 'saturnian-installation-art'));
            ugSpecializationSelect.options.add(new Option('Jovian Performing Arts', 'jovian-performing-arts'));
            ugSpecializationSelect.options.add(new Option('Neptunian Soundscapes', 'neptunian-soundscapes'));
            ugSpecializationSelect.options.add(new Option('Pluto-inspired Poetry', 'pluto-inspired-poetry'));
            ugSpecializationSelect.options.add(new Option('Comet Choreography', 'comet-choreography'));
            // Add more specializations as needed
            break;

    }
}


function updateRating(targetId, value) {
    const ratingValueElement = document.getElementById(targetId);
    if (ratingValueElement) {
        ratingValueElement.textContent = value;
    }
}

const cgpaRatingContainer = document.getElementById('cgpa');
const backlogsRatingContainer = document.getElementById('backlogs');

if (cgpaRatingContainer) {
    cgpaRatingContainer.addEventListener('input', function () {
        updateRating('cgpaRating', this.querySelector('input').value);
    });
}

if (backlogsRatingContainer) {
    backlogsRatingContainer.addEventListener('input', function () {
        updateRating('backlogsRating', this.querySelector('input').value);
    });
}

