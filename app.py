import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


api_key = GENAI_API_KEY


# Configuring generative AI with your API key
genai.configure(api_key=api_key)
# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,

  system_instruction="You are a AI support assistant designed to answer user queries related to the IIT Madras BS program in Data Science and Applications. You should keep the answer consice and only answer related to the degree. If asked any query outside of its problem statement, you will politely inform about your limitations. You should link the information source also. \n\nData Source:\n\nCourses:\n\nThe program is divided into four levels: Foundation, Diploma (Programming or Data Science), BSc Degree, and BS Degree (Data Science and Applications).\n\nEach level has a specific set of courses designed to equip learners with progressively advanced knowledge and skills in data science and related fields.\n\nQualifer level:\nMathematics for Data Science I (BSMA1001)\nStatistics for Data Science I (BSMA1002)\nComputational Thinking (BSCS1001)\nEnglish I (BSHS1001)  \n\nFoundation level:\nMathematics for Data Science II (BSMA1003) *Prerequisite: BSMA1001\nStatistics for Data Science II (BSMA1004) *Prerequisites: BSMA1002, BSMA1001 (Corequisite: BSMA1003)\nProgramming in Python (BSCS1002) *Prerequisite: BSCS1001\nEnglish II (BSHS1002) *Prerequisite: BSHS1001\nDiploma Level\n\nDiploma in Programming\n\nDatabase Management Systems (BSCS2001)\nProgramming, Data Structures and Algorithms using Python (BSCS2002)\nModern Application Development I (BSCS2003) *Prerequisite: BSCS2001\nModern Application Development I - Project (BSCS2003P) *Prerequisite: BSCS2003\nProgramming Concepts using Java (BSCS2005)\nModern Application Development II (BSCS2006) *Prerequisite: BSCS2003\nModern Application Development II - Project (BSCS2006P) *Prerequisites: BSCS2003, BSCS2006\nSystem Commands (BSSE2001)\nDiploma in Data Science\n\nMachine Learning Foundations (BSCS2004)\nBusiness Data Management (BSMS2001)\nBusiness Data Management - Project (BSMS2001P) *Prerequisite: BSMS2001\nMachine Learning Techniques (BSCS2007) *Prerequisite: BSCS2004\nMachine Learning Practice (BSCS2008) *Prerequisites: BSCS2004, BSCS2007\nMachine Learning Practice - Project (BSCS2008P) *Prerequisite: BSCS2008\nBusiness Analytics (BSMS2002) *Prerequisite: BSMS2001\nTools in Data Science (BSSE2002) *Prerequisite: BSCS2004\nBSc Degree Level\n\nCourses not specified in the provided information. Refer to the official program website for details.\nPlease note: This list only includes course names and codes. Refer to the official program website for detailed course descriptions and prerequisites.\n\nTerm Structure:\nThe program follows a flexible term structure, allowing learners to progress at their own pace.\nEach year is divided into three terms: January Term, May Term, and September Term. Each term lasts four months.\nEvery term consists of:\n12 Weeks of Coursework: Learners engage in online video lectures, complete assignments, and participate in discussions during this period.\n2 In-person Invigilated Quizzes: These quizzes are conducted at designated exam centers across India to assess learners' understanding of the course material.\nEnd-Term Exams: Learners take in-person end-term exams at designated exam centers to evaluate their overall learning outcomes for each course. (https://study.iitm.ac.in/ds/academics.html)\n\nRegular Entry Process for IIT Madras BS Degree program in Data Science and Applications:\nThis section details the admission process for regular entry into the program. Here's a breakdown of the key steps:\n\nEntrance exam/Qualifier Process:\nAll regular entry applicants must qualify through the Qualifier Process to gain admission to the Foundation Level.\nThe Qualifier Process involves a 4-week online preparatory course covering foundational topics in English, Mathematics for Data Science, Statistics for Data Science, and Computational Thinking.\nLearners engage in video lectures, assignments, and live sessions during this period. Weekly assignments are mandatory for grading.\nAt the end of 4 weeks, a qualifier exam is conducted to assess learners' understanding of the covered material.\n\nEligibility for Qualifier Exam:\nThe average score of the best 2 out of the first 3 assignments in each course is calculated.\nLearners must achieve a minimum average assignment score in all four courses to be eligible for the Qualifier Exam. The minimum score varies based on the learner's category (General, SC/ST/PwD etc.).\nNote: The relaxed criteria for the Qualifier Process do not apply to the program itself once enrolled.\n\nQualifier Exam and Passing Criteria:\nOnly eligible learners receive a hall ticket for the in-person Qualifier Exam.\nThe 4-hour Qualifier Exam covers all four foundational courses.\nTo pass, learners need to achieve both a minimum average score and a minimum score in each individual course. The minimum score requirements vary based on the learner's category.\nValidity of Qualifier Exam Result:\n\nThe Qualifier Exam result is valid for 3 terms (1 year) for candidates who have cleared class 12 board exams. They can choose to join the program later within this validity period.\nThe validity is extended to 6 terms (2 years) for candidates yet to appear for class 12 exams, allowing them to join after passing class 12.\nLimitations on Foundation Level Course Registration:\nAlthough anyone who passes the Qualifier Exam can register for Foundation Level courses, the number of courses allowed in the first term is limited based on the Average Qualifier Exam Score.\n\nRe-attempting the Qualifier Exam:\nLearners who didn't clear the Qualifier Exam or were absent can re-attempt it in the same term without repeating assignments.\nRe-attempting the exam requires filling an application form and paying a fee (amount varies based on learner category).\nLearners who are not eligible to re-attempt or fail the re-attempt need to re-apply for the next term, going through the entire Qualifier Process again.\n(or)\nJEE-based Entry:\nCandidates qualified to appear for the current year's JEE Advanced exam can directly join the program by completing the application form, paying the admission fee, and registering for Foundation Level courses.\n\nInternational Students:\nThe program is open to international learners.\nIn-person exams are conducted in some countries (UAE, Sri Lanka, Bahrain, Kuwait, Oman). Learners residing in these countries must appear for these exams.\nLearners from other countries can enroll and take remote proctored exams.They can contact ge@study.iitm.ac.in for further information.\n\nAdditional questions:\nDoes IIT Madras offer B.Sc in Programming & Data Science on-campus?\nNo, there is no equivalent on-campus version. IIT Madras has carefully curated this exclusively as an online\n\nWill those enrolled to this program have access to IIT Madras campus facilities?\nDue to limitations of campus facilities and students being spread out geographically, learners enrolled in the program will not have access to IITM campus facilities.\n\nWhat is the language of instruction for these courses? Are they available in other regional languages?\n All our program courses are taught in English. Hence, we expect a minimum proficiency in English language to participate in the program.\n\nI am a CA / B.Com Graduate / Lawyer / B.Sc Graduate / Mechanical engineer / MBBS student and do not have any knowledge of coding. Does this course cover the basics of coding before progressing to advanced levels?\n  It is not necessary to have a prior knowledge of coding to learn from our program. Our program is structured in such a way that once a learner starts from the Foundational level and progresses towards the Degree level, in sequence, he / she will obtain sufficient proficiency in Programming and Data Science.\n\nHow long will it take to complete the online degree program if I am working?\nThe full program can take anywhere between 3 and 6 years to complete. On an average, we anticipate that a learner studying part time will finish the degree in 4 to 5 years. While this is the estimated time for the full degree, a diploma can potentially be obtained faster (around 8 months - 2 years). Check Academics page to better understand the program structure.\n\nWhat are the technological requirements for this program?\nAccess to good internet connection as well as a laptop / desktop device will be a key requirement to learn effectively from our courses. Familiarity with Google tools would be an advantage.\n\nWill the classes be taught live? Will there be any interaction?\nNo. Pre-recorded lessons and assignments will be made available on our portal on a weekly basis. Learners can learn from the content released each week at their own pace, but will be required to submit the weekly assignments online within stipulated deadlines.\nOne or two LIVE sessions per course may be conducted to clear doubts and interact with the course instructor and course support team.\n\n\nWhat is the overall structure of the program? What are Levels?\nThe program is split into three levels that have to be done strictly in sequence:\n1: Foundational Level (8 courses)\n2: Diploma Level (6 Programming courses + 6 Data Science courses)\n3: Degree Level (11 courses)\nCheck Overall Structure in Academics page.\n\nThe expected effort to do well in one course is about 10 hours per week.\n\nHow many courses can I complete in a year?\n There are 3 terms in a year. Learner may be allowed to register for a maximum of 2 - 4 courses in a term depending on their performance in previous exams and their preferred pace of learning.\nNote that all courses of one level need to be completed before registering for courses in the next level, and all prerequisites of a course need to be completed before registering for that course.\n\nHow / where do I ask questions or doubts related to the course content of the program?\n Each course page will have a discussion forum where learners can raise their course-related questions and interact with the course instructor or course support team.\nFor all questions not related to the course, you may write to support@onlinedegree.iitm.ac.in\n\nAre there any communication groups on WhatsApp, Telegram etc for the IITM Online Degree Program?\nWe have NOT created any official groups anywhere yet. We currently answer all questions / doubts via support email / calls.\nWe have plans to create official groups for our learners when the qualifier month starts. We will reach out to you through whatsapp, email and SMS. Kindly look out for communication from our side on this.\n\nAre there any sample video content or assignments?\n As a sample, Week 1 content videos have been made available for the first four Foundational Level courses for you to try and learn from. We recommend you to check out these lectures and try the sample assignment we have put out for each course. The links to Week 1 Content & Assignment pages can be accessed from the Foundational Level courses section in Academics page.\n\nI ran into an error or issue in the application form. What do I do?\nPlease send us your registered email ID and a screenshot of the error / issue with relevant description to support@onlinedegeree.iitm.ac.in\nIf the error is after payment has been made, please forward the confirmation email from Razorpay along with email ID, application number and screenshot with description.\n\nIs there an attendance policy for this program?\n There is no daily attendance, but once you register for the courses, submission of weekly assignment is taken as an attendance indicator. Minimum required scores in weekly assignments of a course will determine if a learner will be allowed to write the end term exam for that course or not.\n\nCan I take my exams from home?\n No. Every term will have 3 quizzes and an end term exam for each course. All quizzes and end term exams will be in-person, invigilated exams at designated centres across the country. You need to travel to the exam centre and take these exams. Check Exam Cities in Academics Page.\n\n A quiz is similar or equivalent to a monthly test in schools and colleges. Marks obtained in quizzes count towards the total score obtained in the course. All quizzes will be in-person, invigilated exams at designated centres across the country.\n\nAre the exam dates flexible?\nNo, the exam dates are not flexible. The quiz and end term exam dates are fixed for all learners taking the same course in a term. We try our best to schedule all exams during the weekends though it may not be possible for every exam.\n\nWhat if I want to request for a city not listed in the current list of exam cities?\n If the city of your choice is not in our current exam cities list, please send an email to support@onlinedegree.iitm.ac.in. We will consider your request, but there is no guarantee that we will add it.\n\nWill there be multiple exam centres within an exam city? How many?\n There may be more than one exam centre in any exam city. The count depends on the number of learners in each city and availability of centres on given date with our exam partner.\n\nWhen will the term start? What is the timeline?\nLearners who clear the Qualifier Exam will be expected to register for the program right after their results are announced. In the first term alone, classes start (with week 5) immediately after the completion of week 4 in the qualifier phase with no gap. Please check Important Dates in Admissions page to get to know the timeline.\n\nCan I pursue only a Diploma instead of Degree?\n Learners who join the IIT Madras Online Degree Program have the option of exiting the program earlier with a Diploma in Programming AND / OR Diploma in Data Science.\nLearners who wish to exclusively pursue a Diploma in Programming OR Data Science alone and already have a basic understanding of the foundations can check out IIT Madras Diploma Program website.\n\nWhat is the eligibility criteria to apply for the Degree Program?\n Check Eligibility section in Admissions page for the latest update of the eligibility criteria.\n\nIs the program available to students currently in class 12 or equivalent?\n Students currently in class 12 (or equivalent) will be allowed to apply for the program, go through the qualifier phase and write the qualifier exam, but will not be allowed to register for the foundational level of the program until they clear class 12 (or equivalent). Note that a Qualifier Exam result is valid only for 3 terms (about 1 year) right after the exam. So, plan accordingly.\n\nI took a break year after class 12 to prepare for JEE / NEET. Can I Apply for the Program?\n Yes, you may apply for the Program if you have studied Mathematics & English in class 10 and have cleared class 12 or equivalent.\n\nI had dropped out of degree over two decades ago. Would I be eligible to apply?\n Yes. If you cleared class 12 or equivalent in 2019 or earlier, you may apply for our program - there is no requirement to have completed a degree program. Check our latest eligibility criteria.\n\nHow and where can I apply for the program?\nAnyone who is eligible may apply by filling in the application form, uploading required documents and paying the application fee.\nWe recommend that you go through the Academics Page to better understand the program and the Admissions Page to understand the admission process before applying.\n\nWhat is the qualifier process?\n All applicants will have to go through a Qualifier Process, like a trial month, wherein they will get access to 4 weeks of content for the four foundational level courses - English I, Mathematics for Data Science I, Statistics for Data Science I and Computational Thinking. Check Qualifier Process in Admissions page\n\n\nWill everyone who goes through the qualifier process be allowed to write the qualifier exam? What is the passing criteria?\nNo. Only the learners who get the minimum required marks in the online assignments during the qualifier process of 4 weeks will allowed to attend the qualifier exam. Only those learners allowed to write the qualifier exam shall be provided with hall tickets.\nRefer to Qualifier Process and the section below it to learn about the minimum required marks in the qualifier assignments and minimum required marks to pass / clear the qualifier exam.\n\nHow long is the qualifier exam result valid for? Can I join the program at a later term if I clear the qualifier exam now?\n The Qualifier Exam result is valid for a period of 3 terms (or 1 year). So, a learner may choose to not register for Foundational Level immediately after clearing the Qualifier Exam and register for the Foundational level in the second or third term following the Qualifier Exam.\n\nHow many times a year will there be admissions? Will it be only once a year?\n For now, we are running applications / admissions thrice a year.\n\nWhat are the documents / files required to apply for the qualifier process of the program?\n The list of required documents is available on the Application Process section of the admissions page.\n\nCan the credits from this online degree program be transferred to learner's college or university (like on the NPTEL platform)?\n IITM's Online BSc Degree in Programming and Data Science is a stand alone program. Credits cannot be transferred.\n\nWill IIT Madras provide the course material for the program in hard copy through courier (like IGNOU)?\n No, the course content will be provided only in online mode so you can watch them anytime, anywhere. There will be no hard copy provided. Depending on the course, learners may be recommended reference books / material that they may buy separately.\n\nCan I submit an older version of the OBC-NCL / EWS certificate while applying or registering for courses?\n Student has to submit valid certificates while applying / registering. These will be verified by our team. An approved certificate will be valid for three terms.\n\nAfter applying, can I get a refund of application fee if I can't write the qualifier exam or if I fail the qualifier exam?\n No. There will be no refund of application fee once paid.\n\nAfter registering for a course in a term, can I carry over the fees to the next term if I am not able to complete the course?\n No. A course registration is valid only for one term. If a learner is not able to clear a course in a term, they will be considered as having failed the course and will need to register for the course again at a later term along with the required fee.\nNote that a learner will be allowed to drop off from a course within the first four weeks of the term. In such cases, a part of the course fee will be retained as admin charges and the balance, if any, may be carried over to the next term\n\nWhat is the Fee structure? Should we submit the entire fees at once or in installments?\n The overall program fees will not be paid at one stretch. The actual fees you will be paying in each term will be in proportion to the number of courses you register for in the respective term. So, if you register for 2 courses in a term, you have to pay the fees only for those 2 courses. For more details, please refer to Fee Structure in Academics Page.\n\nWhat is the mode of payment?\n Fees can be paid only through online mode. Fees through DD will not be accepted.\nNote that payment cannot be made using Debit Card. You can pay using any Credit Card, Netbanking (all Indian Banks), Wallet, UPI (Google Pay, BHIM, etc.).\n\nWill I get any confirmation on successful payment of fee?\n Yes. After successful completion of payment, you will receive a confirmation email from Razorpay.\n\nIf my payment fails, how many days will it take to the money back in my bank account?\n In case of failed payments, it will take 3 to 4 weeks for the money to be credited back in your bank account.\n\nCan I edit my application form after submitting it?\n Your application form will be considered as submitted only upon making the application fee payment. Until then, you may edit the contents of your application form. After the application fee has been paid, you will not be allowed to edit the application form.\nIn case your uploaded document(s) gets \"returned / rejected\" during verification, you will be given a chance to re-upload a valid document within a stipulated deadline.\n\nMy application status says \"Verification Under Process\". How long will it take for my application to be verified?\n Verification of documents may take upto 3 weeks. Please be patient. We will keep you updated about your application status by email / SMS.\n\nHow to avoid getting my application \"returned / rejected\"?\n After you submit your application, we verify the same before changing the status of uploaded document(s) to \"accepted\" or \"returned / rejected\".\nBe careful when filling the application form and double check the information you enter. We verify the files / documents you have uploaded (photograph, signature, ID card, SC / ST / OBC-NCL / EWS / PwD document if applicable). If any of the files / documents uploaded is unclear or broken or found to be wrong or incorrect, your application may be \"returned / rejected\".\nIn case your uploaded document(s) gets \"returned / rejected\" during verfication, you will be given a chance to re-upload a valid document within a stipulated deadline.\nBeing honest and careful while filling the application form and uploading correct documents in the correct formats will help get your application \"accepted\". Check Application Process for required documents, document formats and sizes.\n\nCan I select only one city as my Exam City instead of selecting two preferences?\n No. You will need to pick two different preferences for exam cities in the order of your preference. Your exam centre shall be allotted in any one of the two exam cities picked depending on availability. We recommend that you familiarise with the current available Exam City options to be able to pick your preferred exam cities.\n\nCan I change my exam cities for the qualifier exam after having paid and submitted my application?\n You will not be allowed to change your exam city for the qualifier exam after submitting your preferences in the application form.\nIf there is any unavoidable situation because of which you need to have the qualifier exam city changed, please write to us. We will try to accommodate your request based on availability, but cannot guarantee a change of exam city.\n\nWill the Exam City preferences I select for the Qualifier Exam in the application form be fixed for all the later exams?\n No. The Exam city preferences selected in the application form is for the Qualifier Exam only. You will have the option of picking a different set of Exam City options, if you wish, after qualifying for the later invigilated exams.\n\nWill I get a scholarship / loan for this programme?\n We are trying to see if this is possible. Please watch out for announcements regarding scholarships / loans.\n\nIs there any concession for SC / ST / OBC-NCL / EWS / PwD candidates in terms of scores?\n SC / ST / OBC-NCL / EWS /PwD candidates will have concession in minimum scores required during the qualifier process to enter the program. Check out Qualifier Process in Admissions page. Note that there will be no such concessions after entering the program. (OBC candidates not belonging to the OBC-NCL category cannot avail any concession)\n\n\nIs there any fee waiver for SC / ST / OBC-NCL / EWS / PwD candidates or candidates with lower family income?\n Only SC / ST / PwD candidates may avail fee waivers in the application stage. After clearing the qualifier process and exam, candidates belonging to any category (General / OBC / EWS / SC / ST / PwD) may avail fee waivers in course fees based on family income. Check Fee Structure in Academics page for details.\n\nWhat does \"family income\" in the fee structure mean?\n The term family income for the purpose of availing fee waivers includes the income of the candidate, the income of his/her parents and spouse, also the income of his/her siblings and children below the age of 18 years.\nAfter clearing the Qualifier Exam, all learners who wish to avail fee waivers based on Family Income required to submit Family Income Certificate in the format provided in the Fee Structure section. Note that the Family Income Certificates are valid only for one year and will need to be submitted afresh each year to continue availing fee waiver based on Family Income through the program.\n\nI belong to the general category and I want to avail fee waiver since my family income in below 5 lakhs per annum. Why do I need to submit EWS + Family Income Certificate to avail the waiver?\n Economically Weaker Section (EWS) in India, as defined by the Govt. of India, is a sub-category of people belonging to the General category with an annual family income less than ₹8 lakhs per annum and who do not belong to any category such as SC/ST/OBC. Course fee waivers from IIT Madras are available for general category learners with family income less than ₹5 lakhs per annum. As per the policy of IIT Madras, and as part of our documentation process to ensure that we give fee waiver benefits to the deserving learners, we require general category learners with family income less than ₹5 lakhs per annum to submit both EWS certificate and Family Income certificate. EWS and Family Income certificates will need to be obtained in the format mentioned in the Fee Structure section in Academics page.\n\nWill students who enter the program have internship / recruitment opportunities provided by IIT Madras?\n We will try to make internship / recruitment opportunities available to learners; we will notify learners when the opportunities arise.\n\nHow does IIT Madras plan to provide placements for lakhs of applicants?\n A large number of learners apply and participate in the qualifier process. After clearing the qualifier process, learners will need to clear foundational level courses, diploma level courses and then the degree level courses to finally get a BSc degree from IIT Madras. That's a total of 31 courses of IIT standard and 116 course credits. When a student is able to successfully clear these courses and fulfill all the academic requirements, we are confident that the students will be employable.\n\nDo I get placement opportunities after I complete the BSc Degree?\n The demand for data analysts / scientists and full stack developers is very high. Through our program, we do our best to equip our learners with required subject expertise. We are also planning to give soft skills training as part of the program. It is all about enabling IITM BSc graduates with the right job opportunities. IIT Madras will actively reach out to the recruiters in the context of placement opportunities for the graduates of the Online BSc Degree Program.\n\nWhat is the registration process for the Foundational Level?\n Once you clear the Qualifier Exam, you will be allowed to access the Course Registration Form from your dashboard upon logging in. In the Course Registration Form, you will need to fill the required details, upload necessary documents and pay the course fee to register for the first term of your Foundational Level. You may choose to register for one or more Foundational Level courses with the upper limit of courses you can register for depending on your Qualifier Exam Score.\nNote that there will be an added Exam Fee applicable for learners opting to write their quizzes and end term exams outside India.\n\nWhat are the documents / files that are required to be uploaded while registering for the Foundational Level?\n It is mandatory any one of these documents while registering for Foundational Level:\n- 12th or equivalent mark sheet OR\n- Degree Certificate OR\n- Certificate of the highest level of education\n\nWhat are the documents needed to avail fee waiver at Foundational Level and later?\n Please refer to the Fee Structure section in the Academics page to see which fee waiver may be applicable to you and the relevant documents / certificates that will need to be submitted.\n\nI have already submitted my category certificate while applying for the Qualifier Process. Do I need to submit them again while registering for the Foundational Level?\n No, not required to submit again. However, the EWS / OBC-NCL certificate need to be submitted again if the previously submitted certificate is not valid until the end of the current financial year.\n\nI can't afford to pay the entire Foundational Level fees at one shot and I do not come under any fee waiver category too, can I pay the fees in 2 or 3 installments?\n Please be informed that you will not be paying the entire Program fee or Foundational Level fee at one stretch. The actual fees you will be paying will be in proportion to the number of courses you register for in every term. So, if you register for 2 courses in the January 2021 Term, you have to pay the course fees only for those 2 courses.\nIn the Fee Structure section, select your goal to be able to see a detailed PDF with break down of course fee over each term.\n\nCan I change my email ID in the Foundational Level? Will we get any official student email ID?\n The personal email ID you applied for the program with cannot be changed. This email ID is used to access the whole Qualifier Process and the Foundational Level Course Registration Form.\nOnce all the documents uploaded in the Foundational Level Course Registration Form are approved, each registered learner will be assigned a roll number and a corresponding official IIT Madras Online Degree student email ID. After that, all further communication and course access will be through the official student email ID.\n\nIs it possible to get an educational loan for this Program?\n We are working on the process of getting the bank loans approved for this Program. Please do look out for updates from our side on this.\n\n\nWill I be given a new portal to access courses at Foundational Level?\n No, the current portal will be used for all the Levels. You will be given a new official IITM Online Degree student email ID to access the portal.\n\n\nWill I be issued an ID card?\n An ID card in electronic format will be provided, subject to conditions on use of ID card.\n\nCan I take a break of 1 or 2 year(s) after completing the Foundational Level?\n The BSc Degree has to be completed within a maximum period of 6 years. While a 1 or 2 year break between Levels is allowed, we recommend that you time the length of your breaks depending on whether you want to pursue a Diploma or Degree, and how many courses you are able to take up in a term.\n\nI am unable to attend the Qualifier Exam but received hall ticket / I didn't clear the Qualifier Exam. What will be the procedure to re-apply? Do I need to pay application fee again?\n You can re-apply again for the immediate next Qualifier Process with partial application fee payment. Your previous assignment scores will be considered and you will be directly eligible to write the Qualifier Exam without having to submit assignments again.\n\n\nI applied for the Qualifer Exam but I didn't obtain the minimum required average assignment scores to take Qualifier Exam, and hence didn't receive any hall ticket for the same. What will be the procedure to re-apply?\n You have to re-apply as a new applicant with payment of full application fee.\n\nI'm eligible to apply 4 courses in the upcoming term, but I have only 2 Foundational Level courses left to complete. Will I be allowed to register for Diploma Level courses along with the Foundational Level courses?\n No, you have to complete all the 8 courses in Foundation Level before enrolling to the Diploma Level courses.\n\nWhat is the eligiblity to write the End Term Exam for a course?\n To be eligible to write the End Term Exam for a course, it is mandatory for the learner to have (i) obtained in the course an Average Assignment Score >= 40/100 AND (ii) appeared for at least one out of the three proctored in-person Quizzes.\nLearners who are not eligible to write a specific course's End Term Exam will not be issued hall ticket for the same. They will have to repeat the entire course including assignments and quizzes in a later term.\n\nIs it mandatory to take the proctored in-person Quizzes?\n It is mandatory to attempt at least one of the three proctored in-person quizzes in a term to be eligible to appear for the End Term Exams.\n\nWill Qualifier phase assignment scores be included while calculating the eligilibity for the End Term?\n For the courses you register for immediately after clearing your Qualifier Exam, yes, your Qualifier phase assignment scores will be included while calculating eligibility for the End Term Exam.\nFor courses that you register for in a later term, you will be required to repeat the assignments completed in the Qualifier phase.\n\nWill my Qualifier Exam Score be considered in the subsequent term?\n The Qualifier Exam Score will be counted as Quiz 1 Score for the courses registered in the Foundation level in the term immediately after the Qualifier exam.\n\nWhat will happen if I am absent for an End Term Exam?\n Learner has two options:\n1. Register for the course in the subsequent term with the option of taking the End Term Exam alone and by paying a reduced fee (Rs.1000 per Foundational Level course and Rs.2000 per Diploma / Degree Level Course).\n2. Repeat the entire course (including assignments and quizzes) by paying the full course fee.\n\nWhat is the procedure to add / drop a course?\n Once the registration window closes in any term, adding courses will not be allowed. Dropping a course will be allowed within 4 weeks of the term start\n\nCan I get a refund if I drop a course within the first four weeks of the term start?\n For courses dropped within the first four weeks of the term, admin charges will be retained and the balance course fee, if any, will be refunded. Admin charges for a Foundational Level course is Rs.2000 and the admin charges for a Diploma / Degree Level course is Rs.4000.\nFor learners who registered to take exams outside India, 50% of End Term Exam Fee for the dropped course will be refunded. If such a learner chooses to drop all courses in a term, 50% of Quiz 2 & Quiz 3 fee will also be refunded.\nFor more details, please refer to the operations document shared with registered students named \"Part II - Foundation + Diploma\" under section \"13.7. Dropping a Course\".\n\nIs it possible to repeat a course for improving grades?\n Though it is not recommended, a learner may choose to repeat a course for improving grades any number of times. The course fee for repeating a course will be twice the regular course fee and the learner will have to submit the online graded weekly assignments, appear for the Quiz(zes) and End Term Exam.\nThe highest score among all attempts of a course will be used for calculating the CGPA.\n\nWhat is the procedure to change exam city from UAE(or any foreign countries) to India / India to UAE?\n Please send an email to support@onlinedegree.iitm.ac.in\n\nHow can I change the exam city within India?\n Each exam has a deadline before which change of exam city is allowed. Option to change the exam city will be available till each deadline in the student Dashboard, in the \"Exam Cities and Hall Tickets\" page.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
)

chat_session = model.start_chat(
  history=[
  ]
)

# Making a streamlit page
with st.sidebar:
        st.header("🪄")
        st.subheader("Made by khavindev✨")
        st.write("A student of IIT Madras BS in data science")
        st.write("[My LinkedIn](https://www.linkedin.com/in/s-khavin73/)")
        st.write("[Github](https://github.com/khavindev)")
        st.write("if you have any issues ping me on linkedin")
        st.write("[Powered by gemini-1.5]")



st.title("IIT Madras BS BOT🎓:")
st.subheader("Ask any query about the BS in Data Science Program 📚🔍")
# User input
user_input = st.text_input("💬 Enter your question here : ✍️")

if st.button("Get Response✨"):
    if user_input:
        chat_session = model.start_chat(
            history=[]
        )

        response = chat_session.send_message(user_input)
        st.write(response.text)
    else:
        st.write("Please enter a question.")
