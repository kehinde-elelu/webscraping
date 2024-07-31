# # import re

# html_content = """
# <div aria-labelledby="jobDetails" class="seperate-bottom tab bloc jdp-description-details" id="jdp_description" role="tabpanel">
# <div class="col-2">
# <div class="col big col-mobile-full jdp-left-content">
# <p></p><p><br></p><p><strong>POSITION SUMMARY:</strong></p><br><p>HIAS seeks an ERP Support Analyst, NetSuite to assist in the development and maintenance of the company’s Enterprise Resource Planning System (ERP-NetSuite). This position will assist with the various components of the ERP system, primarily Finance and HR-focused work, including systems and optimization, processes, end user support and training workflows, etc. The ERP Support Analyst, NetSuite also works with the Finance, HR and IT teams to maintain systems configuration settings and features to keep the ERP aligned with business requirements. They will also identify opportunities for ERP improvement and communicate recommendations to management.</p><br><p><strong>ESSENTIAL FUNCTIONS:</strong></p><br><ul>
# <br><li>The position will be responsible for the ERP Finance, IT, and HR subsystems (NSPB, Pyango, ADP, Replicon, Boomi).</li>
# <br><li>Serves as primary liaison with end users and ERP providers; serves as lead and subject matter expert in the ERP applications and related systems.</li>
# <br><li>Reports systems issues to providers and works with them to resolve the issues, documenting processes and results.</li>
# <br><li>Drafts or revises related policies and procedures.</li>
# <br><li>Performs lead responsibilities on an on-going basis for assigned ERP sub-systems; provides support for configuration changes, workflow changes and other system process modifications.</li>
# <br><li>Participates in change management control of ERP systems; works with IT services to control access to ERP systems data; helps provide support for NetSuite ERP through the appropriate Services Help Desk; aids end user on “how to” questions.</li>
# <br><li>Assists in identifying and defining systems and processing alternatives capable of meeting business needs.</li>
# <br><li>Helps maintain data integrity in systems by running queries and analyzing data.</li>
# <br><li>Works with staff to identify information requirements and develops standard reports in NetSuite and NetSuite Planning and Budget for ongoing customer needs and ad hoc queries as needed.</li>
# <br><li>Works with IT staff and provider to resolve complex reporting issues.</li>
# <br><li>Manages changes to the ERP platform to reflect the changing structure of HIAS as it expands.</li>
# <br><li>Plans and provides or arranges training classes for staff as needed on the use of ERP systems; includes initial training for new users, creation of a library of training videos on various procedures in different areas of the system, training on new processes or training to groups on specific functionality; develops user procedures, guidelines and documentation.</li>
# <br><li>Responsible for the improvement and operation of ERP systems connected to the collection, retrieval, accessibility and usage of financial data to facilitate department planning and activities.</li>
# <br><li>Manages end user permissions and access rights in collaboration with IT.</li>
# <br><li>Performs other duties as assigned.</li>
# <br>
# </ul><br><p><strong>QUALIFICATIONS &amp; REQUIREMENTS:</strong></p><br><ul>
# <br><li>Undergraduate degree in Computer Science, Accounting or Finance required; graduate degree preferred.</li>
# <br><li>4-6 years of relevant work experience, with at least 3 years of experience with financial and HR application (ERP) management systems; experience with Oracle NetSuite is required.</li>
# <br><li>Excellent communication (both orally and in writing); Spanish fluency is a plus.</li>
# <br><li>Highly reliable and flexible, with the ability to adapt quickly to various environments and situations.</li>
# <br><li>Excellent interpersonal and problem-solving skills, including a learning mindset and experience with/exposure to coordinating with colleagues across multiple cultures, contexts and time zones to help them address financial or system issues.</li>
# <br><li>Highly organized and detail-oriented; ability to work under pressure, multi-task effectively and meet multiple deadlines in a fast-paced environment.</li>
# <br><li>Strong computer skills, including accounting, budget workflow, approvals and controls for enterprise financial and human resource systems.</li>
# <br><li>Understanding and interpreting financial, budget and human resources system requirements from both a business and technical perspective; knowledge of accounting and budgeting principles to prepare financial reports.</li>
# <br><li>Ability to diagnose and resolve systems analysis problems, evaluate alternatives and make sound independent decisions within established guidelines.</li>
# <br><li>Must have broad knowledge with techniques in collecting data, analyzing information, generating reports, programming and SQL server; open to learning new processes and can translate that knowledge to others.</li>
# <br><li>Prior experience and knowledge of automation/programming and expertise in managing data in relational databases, and the application of data visualization tools (e.g., PowerBI).</li>
# <br><li>Ability to accomplish projects working with and through others, consistently documenting procedures that were undertaken to address a problem.</li>
# <br><li>Experience working at a US government, grant funded non-profit company is preferred, but not required.</li>
# <br><li>Travel, to include travel to insecure operating environments, may be required.</li>
# <br>
# </ul><br><p><strong>HIRING PROCESS:</strong></p><br><p>We are committed to a fair and respectful hiring process, and we do our absolute best to respond to every applicant. We prioritize communication and transparency with all candidates, even those who are not moving forward. Here’s a snapshot of our hiring process:</p><br><p>Step 1: Submit your application!</p><br><p>Step 2: Phone screen with a HIAS recruiter.</p><br><p>Step 3: Video interview with the hiring manager.</p><br><p>Step 4: Video interview with a panel of HIAS employees.</p><br><p>Step 5: Online reference check with SkillSurvey.</p><br><p>Step 6: Offer and background check with Shield Screening or HireRight.</p><br><p>Step 7: Start your professional journey with HIAS!</p><br><p><em>Note: Some of our hiring processes may vary, and not all candidates will advance to each step.</em></p><br><p><strong>ABOUT US:</strong></p><br><p>Over one hundred years ago, the Jewish community founded HIAS (originally the Hebrew Immigrant Aid Society) in New York City, the immigrant gateway to America. Supporting Jews fleeing persecution and poverty in Eastern Europe, our founders were guided by the traditions, texts and history of the Jewish people—a history of oppression, displacement and diaspora. HIAS has since helped generations of Jews facing violence because of who they were, and HIAS remains committed to helping Jewish refugees anywhere in the world. Today, our clients at HIAS come from diverse faiths, ethnicities and backgrounds, as do our staff. We bring our experience, history and values to our work across five continents, ensuring that refugees today receive the vital services and opportunities they need to thrive.</p><br><p>HIAS is a learning community, committed to diversity and inclusion. We do our work with integrity, accountability, transparency and a commitment to the highest ethical standards. We seek employees from diverse backgrounds and life experiences to join our teams located in the United States and across the globe. People who identify as BIPOC, people with disabilities, people from the LGBTQ+ community and people with lived experiences of forced displacement or immigration are all encouraged to apply. We are committed to building a diverse workforce that reflects our vision, mission and values.</p><br><p><strong>VISION:</strong></p><br><p>HIAS stands for a world in which refugees find welcome, safety and opportunity.</p><br><p><strong>MISSION:</strong></p><br><p>Drawing on our Jewish values and history, HIAS provides vital services to refugees and asylum seekers around the world and advocates for their fundamental rights so they can rebuild their lives.</p><br><p><strong>VALUES:</strong></p><br><p><em>Welcome • Acogimiento • Hospitalité • Hachnasat Orchim</em></p><br><p>We <strong>Welcome</strong> the Stranger</p><br><p><em>Justice • Justicia • Justice • Tzedek</em></p><br><p>We Pursue <strong>Justice</strong></p><br><p><em>Empathy • Empatía • Empathie • Chesed</em></p><br><p>We Approach our Clients with <strong>Empathy</strong></p><br><p><em>Partnership • Compañerismo • Coopération • Chevruta</em></p><br><p>We Believe in Changing the World through <strong>Partnership</strong></p><br><p><em>Courage • Coraje • Courage • Ometz</em></p><br><p>We Act with <strong>Courage</strong> to Build a Better World</p><br><p><em>Resilience • Resiliencia • Résilience • Ruach</em></p><br><p>We Adapt and Thrive, Continuously Demonstrating our <strong>Resilience</strong></p><br><p><strong>DIVERSITY:</strong></p><br><p>HIAS is committed to a diverse and inclusive workplace. As an equal opportunity employer, all qualified applicants will be considered for employment without regard to race, color, national origin, ethnic background, ancestry, citizenship status, religious creed, age, sex, gender, sexual orientation, physical disability, mental disability, medical condition, genetic information, marital status, registered domestic partner or civil union status, familial status, pregnancy, childbirth, military status, protected veteran status, political orientation or other legally protected status.</p><br><p><strong>SAFEGUARDING:</strong></p><br><p>HIAS is committed to the protection of children, vulnerable adults and any other person from any harm caused directly or indirectly due to their coming into contact with HIAS. We will not tolerate sexual exploitation, abuse or any form of child abuse or neglect by our staff or associated personnel. Any candidate offered a job with HIAS will be expected to sign and adhere to HIAS’ Code of Conduct and Safeguarding policies. All offers of employment will be subject to satisfactory references and appropriate screening checks, which can include criminal records. HIAS also participates in the </p><div class="anchor-hijack" style="display: inline"><a href="http://#" class="exLink" exlinkattribute="http://#" target="_blank" rel="nofollow ugc"><button class="content-reveal-button btn btn-naked np mt10 b" style="font-weight: bold;">Click To Reveal Url</button></a></div>. In line with this Scheme, we will request information from job applicants’ previous employers about any findings of sexual exploitation, sexual abuse and/or sexual harassment during employment, or incidents under investigation when the applicant left employment. Likewise, HIAS will share this information when other organizations inquire about current and former HIAS staff as part of their recruitment process. By submitting an application, the job applicant confirms their understanding of these recruitment procedures.<br><br><br><b>How to apply</b><br><br><p>Please submit your resume, cover letter and application to our website: </p><div class="anchor-hijack" style="display: inline"><a href="http://#" class="exLink" exlinkattribute="http://#" target="_blank" rel="nofollow ugc"><button class="content-reveal-button btn btn-naked np mt10 b" style="font-weight: bold;">Click To Reveal Url</button></a></div><br><br><br><p>Deadline: 16-Feb-24</p><br><br>#J-18808-Ljbffr
# <div class="bloc jdp-required-skills">
# <h3 class="dark-blue-text pb">Recommended Skills</h3>
# <ul class="pl0 no-marker">
# <li class="check-bubble">Adaptability</li>
# <li class="check-bubble">Attention To Detail</li>
# <li class="check-bubble">Automation</li>
# <li class="check-bubble">Business Requirements</li>
# <li class="check-bubble">Change Management</li>
# <li class="check-bubble">Communication</li>
# </ul>
# </div>

# </div>
# <div class="col small col-mobile-full seperate-top-border-mobile" id="col-right">

# <div id="ads-mobile-placeholder"></div>




# </div>
# </div>
# <div class="seperate hide-mobile" id="apply-bottom-content">
# <div id="apply-bottom" style="top: 2450px; bottom: auto;">
# <div class="col-2">
# <div class="col big col-mobile-full">
# <h3 class="fz1rem">Apply to this job.</h3>
# Think you're the perfect candidate?
# </div>
# <div class="col small col-mobile-full">
# <button name="button" type="button" aria-haspopup="dialog" aria-controls="external-apply-hybrid" aria-label="Apply on company website" class="external-apply-link btn btn-linear btn-linear-green btn-block btn-alone" data-gtm="job-action|apply-external-bottom">Apply on company site</button>

# </div>
# </div>
# </div>
# </div>
# <div id="ads-desktop-placeholder"><div class="seperate-bottom bloc center" id="banner-ad">
# <div id="div-gpt-ad-1600875440430-0" style="width: 728px; height: 90px;">
#   <script>
#     googletag.cmd.push(function() { googletag.display('div-gpt-ad-1600875440430-0'); });
#   </script>
# </div>

# </div>
# </div>
# <div data-did="j3n2q1669hdn0dy0pd7" id="partner-jobs-placeholder"></div>

# <div class="seperate-bottom" id="cb-tip" style="top: 0px;">
# <p>
# Help us improve CareerBuilder by providing feedback about this job:
# <button name="button" type="button" class="report-job-link btn btn-naked medium-font-i pl0" aria-haspopup="dialog" aria-label="Report this job" aria-controls="report-job-modal-wrapper" data-did="j3n2q1669hdn0dy0pd7">Report this job</button>
# </p>
# <p class="seperate-bottom normal">Job ID: iviwu78</p>
# <p class="site-tip">CareerBuilder TIP</p>
# <p>
# For your
# <a href="https://www.careerbuilder.com/privacy">privacy and protection</a>,
# <span>when applying to a job online, never give your social security number to a prospective employer, provide credit card or bank account information, or perform any sort of monetary transaction.</span>
# <a href="https://www.careerbuilder.com/privacy">Learn more.</a>
# </p>
# <p>
# By applying to a job using CareerBuilder you are agreeing to comply with and be subject to the CareerBuilder
# <a href="https://www.careerbuilder.com/terms">Terms and Conditions</a>
# for use of our website. To use our website, you must agree with the
# <a href="https://www.careerbuilder.com/terms">Terms and Conditions</a>
# and both meet and comply with their provisions.
# </p>
# </div>
# </div>
# """

# # # Define regex patterns for the job description and job requirements
# # requirements_pattern = re.compile(r"(?<=QUALIFICATIONS & REQUIREMENTS:).*?(?=HIRING PROCESS:)", re.DOTALL)


# # # Extract job description
# # job_description_match = description_pattern.search(html_content)
# # job_description = job_description_match.group(0).strip() if job_description_match else "Job description not found."

# # # Extract job requirements
# # job_requirements_match = requirements_pattern.search(html_content)
# # job_requirements = job_requirements_match.group(0).strip() if job_requirements_match else "Job requirements not found."

# # print("Job Description:")
# # print(job_description)
# # print("\nJob Requirements:")
# # print(job_requirements)



# # from bs4 import BeautifulSoup

# # def remove_html_tags(html_content):
# #     soup = BeautifulSoup(html_content, "lxml")
# #     return soup.text

# # # html_content = "<p>This is a <b>sample</b> text with <a href='#'>HTML</a> tags.</p>"
# # clean_text = remove_html_tags(html_content)
# # print(clean_text)  # Output: This is a sample text with HTML tags.


import re

text = """
You’ll be rewarded and recognized for your performance in an environment that will challenge you and give you clear direction on what it takes to succeed in your role as well as provide development for other roles you may be interested in.Required Qualifications:
Active NP or PA license or ability to obtain by start date.  Licensure must be unencumbered, free of any open/unresolved disciplinary actions including probation or restrictions against privilege to practice
For NPs - Active ANCC or AANP national certification in Family, Geriatrics, Adult, Adult-Gerontology Primary Care, or Adult-Gerontology Acute Care certification OR for PAs - Physician Assistant national certification through NCCPA
Ability to complete physical requirements of the job including lifting a 30-pound bag in and out of the car, navigating stairs and a variety of dwelling conditions, and sit, stand and kneel to perform physical assessment
Reliable transportation to complete home visit assessments 

Preferred Qualifications:
1+ years of clinical experience in their highest level of education, clinical setting 
Experience in Gerontology, Cardiology, Internal medicine, or Endocrinology 
Home Health care or home visit experience 
May be requested to obtain additional licensure in other geographic areas 
Ability to travel up to 5% within licensed states if requested for additional incentives (with notice, based on business needs)

**PLEASE NOTE** Employees must be in an active regular status. Employees must remain in role for a minimum of 12 months from the date of hire /rehire/transfer.  If an employee leaves Home and Community, the student loan repayments will cease. The employee must remain in an Advanced Practice Clinician or Physician role within Home and Community for 36 months to receive the full benefit of the student loan repayments.At UnitedHealth Group, our mission is to help people live healthier lives and make the health system work better for everyone. We believe everyone–of every race, gender, sexuality, age, location and income–deserves the opportunity to live their healthiest life. Today, however, there are still far too many barriers to good health which are disproportionately experienced by people of color, historically marginalized groups and those with lower incomes. We are committed to mitigating our impact on the environment and enabling and delivering equitable care that addresses health disparities and improves health outcomes — an enterprise priority reflected in our mission.Diversity creates a healthier atmosphere: UnitedHealth Group is an Equal Employment Opportunity/Affirmative Action employer and all qualified applicants will receive consideration for employment without regard to race, color, religion, sex, age, national origin, protected veteran status, disability status, sexual orientation, gender identity or expression, marital status, genetic information, or any other characteristic protected by law.UnitedHealth Group is a drug-free workplace. Candidates are required to pass a drug test before beginning employment.
"""

# Split the text into two parts
parts = text.split("Preferred Qualifications:")
print(parts[0])
print("========")
print(parts[1])

# # Keep the first part and the text after "**PLEASE NOTE**"
# cleaned_text = parts[0] + parts[1].split("**PLEASE NOTE**")[1]

# print(cleaned_text)
