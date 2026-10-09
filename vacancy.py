#!/usr/bin/env python3
"""
Vacancy Launcher
----------------
A simple PySide6 launcher for career pages, job portals, universities,
and industry-specific employers.

To add a new website:
    1. Find the most appropriate category in CAREER_SITES.
    2. Add one line:
           "Company Name": "https://example.com/careers",
    3. Keep the trailing comma.

The category order below is intentionally grouped by industry/domain.
"""

import sys
import webbrowser

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QGroupBox,
    QScrollArea,
)

# CAREER DATABASE

CAREER_SITES: dict[str, dict[str, str]] = {
    "01 — Universities, Higher Education & Academic Careers": {
        'University of Kelaniya': 'https://www.kln.ac.lk/vacancies',
        'University of Sri Jayewardenepura': 'https://www.sjp.ac.lk/category/vacancies/',
        'University of Peradeniya': 'https://eng.pdn.ac.lk/vacancies/',
        'University of Ruhuna': 'https://www.ruh.ac.lk/index.php/en/component/sppagebuilder?view=page&id=55',
        'NSBM Green University': 'https://www.nsbm.ac.lk/careers/',
        'SLTC Research University': 'https://sltc.ac.lk/resources/careers/',
        'University of Moratuwa': 'https://uom.lk/vacancies',
        'Faculty of Technology - University of Colombo': 'https://tech.cmb.ac.lk/category/vacancies/',
        'University of Colombo': 'https://cmb.ac.lk/category/vacancies',
        'University of Colombo School of Computing': 'https://ucsc.cmb.ac.lk/vacancies/',
        'SLIIT': 'https://www.sliit.lk/engage/careers-at-sliit',
        'Open University': 'https://ou.ac.lk/vacancies/',
    },
    "02 — Government, Public Sector & Government Technology": {
        'GovJobs.lk': 'https://govjobs.lk/',
        'Government Jobs Gazette': 'https://www.gazette.lk/government-jobs',
        'Gov Jobs': 'https://www.rajayejobs.com/',
        'GovTech': 'https://www.govtech.lk/',
    },
    "03 — Job Portals, Career Aggregators & General Vacancy Sites": {
        'Top Jobs': 'https://www.topjobs.lk/index.jsp/',
        'XPress Jobs': 'https://xpress.jobs/',
        'Rooster Jobs': 'https://rooster.jobs/',
        'Guruwaraya': 'https://www.guruwaraya.lk/2026/03/www.guruwaraya.lk',
        'Remote Jobs': 'https://jobgether.com/remote-jobs/sri-lanka/embedded-systems-and-hardware',
    },
    "04 — Scholarships, Postgraduate Study & Education Opportunities": {
        'Ministry of Education': 'https://mohe.gov.lk/index.php?lang=en',
        'MOHE: Post graduate scholarships': 'https://mohe.gov.lk/index.php?option=com_content&view=category&layout=blog&id=41&Itemid=208&lang=en',
        'Study Sri Lanka: MSc Programs': 'https://www.studysrilanka.org/',
    },
    "05 — Telecommunications, Networking & Communications": {
        'Dialog': 'https://hcmcloud.dialog.lk/CareerPortal/Careers?q=bEopnWmcv9llMiBG3zygOw%3D%3D',
        'Hutch': 'https://hutch.lk/careers/#section2',
        'Huawei Technologies': 'https://www.linkedin.com/company/huawei-technologies-lanka-co-pvt-ltd/jobs/',
        'Sierra Telecommunications': 'https://construction.sierra.lk/service/telecommunication-engineering/',
        'Dar E Com': 'https://www.dar.lk/en/',
        'Superloop': 'https://www.superloop.com/careers/',
        'ZTE lanka': 'https://www.linkedin.com/company/zte-devices-sri-lanka/home/',
    },
    "06 — SLT-MOBITEL Group": {
        'SLT Careers': 'https://www.slt.lk/en/careers',
        'SLT Internship': 'https://embryo.slt.lk/internshipform',
        'SLT Careers Portal': 'https://careers.slt.lk/Home/Join?Length=0',
        'SLTMobitel Careers': 'https://sltmobitel.lk/career?page=1',
        'Mobitel Careers': 'https://www.mobitel.lk/careers',
        'New SLT Careers Portal': 'https://sltmobitel.lk/career?page=1&lan=en',
    },
    "07 — Embedded Systems, Firmware, IoT & Product Engineering": {
        'SenzMate': 'https://www.senzmate.com/company/careers/',
        'Zebra Technologies': 'https://careers.zebra.com/careers/*/colombo_sri_lanka?domain=zebra.com',
        'MagicBit': 'https://magicbit.cc/careers/',
        'Idea8': 'https://www.linkedin.com/company/idea8solutions/jobs/',
        'Iconic Devices': 'https://www.icd.lk/',
        'Protonest IoT': 'https://www.protonest.co/careers',
        'Theekshana RnD': 'https://www.theekshana.lk/',
        'Thakshana Technologies': 'https://www.linkedin.com/company/thakshana-technologies-private-limited/jobs/',
        'Paraqum': 'https://www.paraqum.com/',
        '99x IoT': 'https://99x.io/careers',
        'Azend Technologies': 'https://azendtech.com/careers/',
        'Incbotic': 'https://www.linkedin.com/company/incbotic/posts/?feedView=all',
        'SIoT Services Pvt Ltd': 'https://www.linkedin.com/company/sierraiot/posts/?feedView=all',
        'E Gravity Solutions (Pvt) Ltd': 'https://www.linkedin.com/company/e-gravity-solutions/posts/?feedView=all',
        'Shift Solutions': 'https://www.linkedin.com/jobs/view/embedded-software-engineer-qt-qml-embedded-linux-at-shift-solutions-ltd-4433451838/',
        'Boffo System Labs': 'https://www.linkedin.com/company/boffosys/posts/',
        'Utech IIoT': 'https://utech.lk/',
        'ThingsNode': 'https://www.linkedin.com/company/thingsnodeforindustry/people/',
        'E vision microsystems': 'https://www.linkedin.com/company/evisionmicro/',
        'E wis Pvt Ltd': 'https://ewisl.net/careers',
        'Vortex Labs': 'https://vortexlabsofficial.com/',
    },
    "08 — Electronics Manufacturing, PCB/EMS & Components": {
        'TOS lanka': 'https://toslanka.com/',
        'Elocan lanka': 'https://elcoanlanka.com/',
        'Synopsys': 'https://synopsys.avature.net/careers/SearchJobs/?2001=21393&2001_format=3135&listFilterMode=1&jobRecordsPerPage=6&',
        'ACCLER': 'https://www.linkedin.com/company/accelr-net/jobs/',
        'GPV Lanka': 'https://gpvlanka.recruitee.com/',
        'Aptinex': 'https://www.linkedin.com/company/aptinex-pvt-limited/posts/?feedView=all',
    },
    "09 — Industrial Automation, Instrumentation & Control Systems": {
        'G Flow Instruments': 'https://www.linkedin.com/company/gflowplus/posts/',
        'Hi Tech Solutions': 'https://www.hitech.lk/',
        'Vario Systems': 'https://www.variosystems.com/en/career/vacancies/',
        'Analytical Instruments': 'https://water.aipl.lk/careers/',
        'Jacques Technologies': 'https://jacques.com.lk/were-hiring/',
        'Flintec Systems': 'https://www.flintec.com/company/contact',
        'RCS2 Technologies': 'https://www.linkedin.com/company/rcs-to-technologies/',
        'Emmanuels Lanka - Ja-Ela': 'https://www.linkedin.com/company/emmanuel-s-lanka-pvt-ltd/home/',
        'Cosmos Automation Systems': 'https://www.cosmos.lk/cosmos/about/',
        'NextGen Engineers Technology': 'https://www.linkedin.com/company/nexxtgenengineersforce/jobs/',
    },
    "10 — AI, Machine Learning, Data & Computer Vision": {
        'H2O Ai': 'https://h2oai.applytojob.com/apply/',
        'Rootcode': 'https://rootcode.io/careers',
        'Spera Labs': 'https://www.speralabs.com/careers',
        'Upview Technologies': 'https://upview.tech/careers',
        'Veyrion': 'https://veyrion.com/careers',
        'Innodata': 'https://www.linkedin.com/jobs/search/?currentJobId=4408809227&f_C=89808692&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=4408809227%2C4405529352%2C4398698841%2C4402457235%2C4406490970%2C4401634120%2C4407268808%2C4404668757%2C4399369125',
        'Alta Vision': 'https://www.linkedin.com/company/altavisionltd/posts/?feedView=all',
    },
    "11 — Robotics, Drones & Autonomous Systems": {
        'Liquid Labs': 'https://www.liquidlabs.agency/#careers',
        'Envoy Ortus': 'https://www.linkedin.com/company/envoyortus/jobs/',
        'Scouts Autonomous Drones': 'https://www.linkedin.com/company/scoutsapp/posts/?feedView=all',
        'Surge Robotics': 'https://surge.global/careers/',
        'SimCentric Sri Lanka': 'https://www.linkedin.com/jobs/view/3068966822/',
        'Sri Lanka Institute of Robotics': 'http://slir.lk/',
    },
    "12 — Software Engineering, SaaS & IT Services": {
        'MBiz Software': 'https://mbizsoftware.com/careers/',
        'Tetherfi': 'https://www.linkedin.com/company/tetherfi/jobs/',
        'Axiata Digital Labs': 'https://www.careers-page.com/axiata-digital-labs',
        'hSenid Lanka': 'https://hsenidlanka.com/careers/',
        'MillenniumIT ESP': 'https://www.careers-page.com/mitesp',
        'HCLTech Sri Lanka': 'https://careers.hcltech.com/go/Sri-Lanka/9555555/',
        'Arimac': 'https://careers.siddhify.io/',
        'eConsulate': 'https://econsulate.net/careers/jobs.html',
        'DMS Software Technologies': 'https://www.dmsswt.com/career.html',
        'Atlas Labs': 'https://rooster.jobs/24',
        'Codimite': 'https://codimite.ai/careers/#openings-section',
        'Zone24x7': 'https://zone24x7.com/careers/#available-open-jobs',
        'CodeGEN': 'https://codegen.co.uk/careers',
        'Sysco LABS': 'https://wd5.myworkdaysite.com/recruiting/sysco/syscocareers/jobs?locations=b014cc62fe6601b8d666502cd5287f36',
        'Orel IT': 'https://orelit.com/join-us/',
        'Nagarro': 'https://www.nagarro.com/en/careers/sri-lanka',
        'Hype Invention': 'https://boards.rooster.jobs/13033',
        'I Labs': 'https://www.ilabs.lk/careers',
        'dijital team': 'https://www.dijitalteam.lk/careers',
        'H Connect International': 'https://hconnectint.com/join-us/',
        'i Vedha': 'https://ivedha.com/careers/?job__location_spec=sri-lanka',
        'Kasper Global': 'https://www.kasperworld.com/',
        'Qualqem': 'https://qualqem.com/',
        'SilverLine IT': 'https://silverlineit.co/siportal/',
        'Invenza': 'https://www.linkedin.com/company/invenza-digital-technologies/jobs/',
        'WSO2': 'https://wso2.com/careers/#availableposition',
        'Virtusa': 'https://www.virtusa.com/careers/job-search',
        'Fortude': 'https://careers.fortude.co/#',
        'Spill Labs': 'https://www.spillabs.com/careers/',
        'Ascentic': 'https://rooster.jobs/8728',
        'Frontwalker': 'https://www.linkedin.com/company/frontwalkersl/jobs/',
        'VitalHub': 'https://vitalhub.bamboohr.com/careers?source=aWQ9MzA=',
        'Adveccio': 'https://www.adveccio.com/careers',
        'John Keells IT': 'https://careers.keells.com/JohnKeellsIT/search/?createNewAlert=false&q=&locationsearch=',
    },
    "13 — Cybersecurity, Identity, Biometrics & Physical Security Technology": {
        'Cenmetrix': 'https://www.linkedin.com/company/cenmetrix/people/?facetCurrentFunction=8',
    },
    "14 — Agritech, Agriculture & Food Technology": {
        'SenzAgro': 'https://senzagro.com/careers/',
        'Cresco IoT': 'https://app.crescoagri.com/careers',
        'Ceylon Agro Food Technologies': 'https://www.linkedin.com/company/ceylon-agro-food-technologies-pvt-ltd/posts/',
    },
    "15 — Energy, Power, Renewable Energy & Smart Grid": {
        'Gallion3 IoT': 'https://gallion3.com/',
    },
    "16 — Engineering, Construction, MEP & Industrial Services": {
        'Fame Global': 'https://famegroup.lk/#',
        '3S Fabrications': 'https://www.srilankabusiness.com/exporters-directory/company-profiles/3-s-fabrications-pvt-ltd/',
        'Hayleys Fentons': 'https://hayleysfentons.com/careers/',
        'Maga Engineering': 'https://www.maga.lk/people/careers/',
        'MetG': 'https://www.linkedin.com/company/methg-pvt-ltd/posts/?feedView=all',
    },
    "17 — Automotive, Mobility, EV & Transport": {
        'John Keels CG Auto - BYD': 'https://www.johnkeellscgauto.com/',
        'DIMO': 'https://www.dimolanka.com/careers-and-people/vacancies/',
        'David Peiris Motor Company': 'https://www.dpg.lk/careers/current-openings',
        'Volt Charge': 'https://www.linkedin.com/company/voltcharge-sl/posts/?feedView=all',
    },
    "18 — Manufacturing, Apparel, Materials & Consumer Products": {
        'Brandix': 'https://careers.brandix.com/go/All-Current-Job-Openings/507244/?q=&sortColumn=referencedate&sortDirection=desc',
        'MAS Holdings': 'https://egmh.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs?sortBy=POSTING_DATES_DESC',
        'Phoenix Industries': 'https://phoenix.lk/careers/',
        'Michelin': 'https://michelinhr.wd3.myworkdayjobs.com/en-US/Michelin?Location_Country=db69e062446c11de98360015c5e6daf6',
    },
    "19 — Healthcare, Medical Devices & Life Sciences": {
        'Jendo Innovations': 'https://jendo.health/',
        'Inivos': 'https://www.inivosglobal.com/careers#openings',
        'Technomedics': 'https://www.technomediclk.com/careers.php',
        'HRC Labs': 'https://www.healthreconconnect.com/careers/#job_listings',
        'Sunshine Medical': 'https://www.sunshineholdings.lk/careers/',
    },
    "20 — Finance, Banking, Insurance, Capital Markets & Business Services": {
        'LSEG': 'https://lseg.wd3.myworkdayjobs.com/Careers?locationCountry=db69e062446c11de98360015c5e6daf6',
    },
    "21 — Enterprise Services, BPO, HR & Professional Services": {
        'Renrui': 'https://www.linkedin.com/company/%E6%88%90%E9%83%BD%E4%BA%BA%E7%91%9E%E9%9B%86%E5%9B%A2/jobs/',
        'WNS': 'https://www.linkedin.com/company/wns-global-services/jobs/',
        'In Talent Asia': 'https://intalent.asia/current-vacancies/',
        'John Keells Group Jobs': 'https://careers.keells.com/go/All-Jobs/516610/',
        'John Keells Office Automation': 'https://careers.keells.com/JKOA/search/?createNewAlert=false&q=&locationsearch=',
        'InfoMate': 'https://careers.keells.com/InfoMate/search/?createNewAlert=false&q=&locationsearch=',
        'Aventude': 'https://www.aventude.com/join-us/careers.html',
        'Metropolitan': 'https://www.metropolitan.lk/careers.html',
    },
    "22 — Retail, FMCG, Consumer Brands & Conglomerates": {
        'Browns Group': 'https://simplifiedhr.brownsgroup.com/CareerPageweb',
        'Browns Group Main Careers': 'https://www.brownsgroup.com/careers/',
        'Capital Maharaja': 'https://career44.sapsf.com/career?company=thecapital&career%5fns=job%5flisting%5fsummary&navBarLevel=JOB%5fSEARCH&site=VjItKzkrMlJwaDc4YktCQng3STJwOXN4Zz09&_s.crb=Svjg0o%2f2RBJOdfxz79j37VKTPqPfeReosbrvhPifNYw%3d',
        'Elephant House': 'https://careers.keells.com/ElephantHouse/go/Careers-at-Elephant-House/516910/',
        'Elephant House Main Careers Page': 'https://www.elephanthouse.lk/corporate/careers/vacancies.html?locale=en_GB',
        'Unilever': 'https://careers.unilever.com/en/search-jobs/Sri%20Lanka/34155/2/1227603/7x75/80x75/100/2',
        'Softlogic': 'https://www.softlogic.lk/careers',
    },
    "23 — Aviation, Travel, Tourism & Hospitality": {
        'Agoda': 'https://careersatagoda.com/',
        'SriLankan Airlines Careers': 'https://recruit.srilankan.com/jobs/Careers',
        'SriLankan Airlines Cabin Crew': 'https://srilankan.zohorecruit.com/jobs/slc',
        'Careers page': 'https://www.airport.lk/aasl/careers/careers',
    },
    "24 — Research, R&D, Science & Technology Institutes": {
        'Advanced Research Computing Lanka': 'https://www.arescomp.com/careers/',
        'NERD': 'https://nerdc.lk/projects-services/special-projects/',
        'Arthur C Clarke Institute': 'https://www.accimt.ac.lk/contact-us/job-vacancies/',
        'Centre for Research and Development Ministry of Defense': 'https://crd.lk/vacancies/',
    },
}



# ============================================================================
# UI
# ============================================================================

class VacancyLauncher(QWidget):
    """Main window for the career/vacancy launcher."""

    WINDOW_TITLE = "Vacancy Launcher"
    WINDOW_X = 200
    WINDOW_Y = 120
    WINDOW_WIDTH = 550
    WINDOW_HEIGHT = 700

    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setGeometry(
            self.WINDOW_X,
            self.WINDOW_Y,
            self.WINDOW_WIDTH,
            self.WINDOW_HEIGHT,
        )

        self.build_ui()
        self.apply_theme()

    def build_ui(self):
        """Build the main application layout."""

        main_layout = QVBoxLayout(self)

        # --------------------------------------------------------------------
        # Header
        # --------------------------------------------------------------------
        title = QLabel("Careers / Vacancy Launcher")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            "font-size: 20px; "
            "font-weight: bold; "
            "margin: 8px;"
        )
        main_layout.addWidget(title)

        subtitle = QLabel(
            "Click a button to open the relevant careers page"
        )
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet(
            "font-size: 12px; "
            "margin-bottom: 8px; "
            "color: #444;"
        )
        main_layout.addWidget(subtitle)

        # --------------------------------------------------------------------
        # Scrollable category area
        # --------------------------------------------------------------------
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()
        container_layout = QVBoxLayout(container)

        for category_name, sites in CAREER_SITES.items():
            category_box = self.create_category_box(
                category_name,
                sites,
            )
            container_layout.addWidget(category_box)

        # --------------------------------------------------------------------
        # Quick actions
        # --------------------------------------------------------------------
        bottom_box = QGroupBox("Quick Actions")
        bottom_layout = QHBoxLayout()

        btn_open_all = QPushButton("Open All Sites")
        btn_open_all.setMinimumHeight(42)
        btn_open_all.clicked.connect(self.open_all_sites)

        bottom_layout.addWidget(btn_open_all)

        bottom_box.setLayout(bottom_layout)
        container_layout.addWidget(bottom_box)
        container_layout.addStretch()

        scroll.setWidget(container)
        main_layout.addWidget(scroll)

    def create_category_box(self, category_name, sites):
        """Create one category box containing website buttons."""

        box = QGroupBox(category_name)
        layout = QVBoxLayout()

        for site_name, url in sites.items():
            button = QPushButton(site_name)
            button.setMinimumHeight(38)

            # Capture this button's URL.
            button.clicked.connect(
                lambda checked=False, link=url: self.open_site(link)
            )

            layout.addWidget(button)

        box.setLayout(layout)
        return box

    @staticmethod
    def open_site(url):
        """Open a career page in a new browser tab."""
        webbrowser.open_new_tab(url)

    @staticmethod
    def open_all_sites():
        """Open every saved career link in the default browser."""
        for sites in CAREER_SITES.values():
            for url in sites.values():
                webbrowser.open_new_tab(url)

    def apply_theme(self):
        """Apply the application stylesheet."""

        self.setStyleSheet(
            """
            QWidget {
                background-color: #f4f6f8;
                color: #111111;
                font-size: 13px;
            }

            QGroupBox {
                border: 1px solid #cfd8dc;
                border-radius: 10px;
                margin-top: 10px;
                padding: 10px;
                background: white;
                font-weight: bold;
            }

            QPushButton {
                background-color: #1976d2;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1565c0;
            }

            QPushButton:pressed {
                background-color: #0d47a1;
            }

            QLabel {
                color: #0b3d91;
            }
            """
        )


# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

def main():
    app = QApplication(sys.argv)
    window = VacancyLauncher()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
