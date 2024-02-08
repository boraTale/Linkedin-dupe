import numpy as np

class Company:
    
    """
    A class to represent a company
    
        instance Attributes:
            name: the name of the company as a string
            location: the location of that company as a string 
            
   """
   
    def __init__(self, name:str,location:str):
        
        """
        Constructs all the necessary attributes for the Company object.
        
            Parameters:
                name: name of the Ccompany (string)
                location: the location of the company (string)
                
            Returns:
                NoneType
                
            exemples:  
            >>>Company1=Company("MCGILL","MONTREAL")
            >>>Company1.name
            'MCGILL'
            >>>Company1.location
            'MONTREAL'
            
            >>>Company2=Company("MyCompany","Laval")
            >>>Company2.name
            'MyCompany'
            >>>Company2.location
            'Laval'
            
            >>>Company3=Company("Plombing","1234 Dudemaine,Montreal")
            >>>Company3.name
            'Plombing'
            >>>Company3.location
            '1234 Dudemaine,Montreal'
       """
       
        self.name=name
        self.location=location
    
    def __str__(self):
        
        """
        Is the formating of a string for Company
        
            Parameters:
                
            Returns:
                Returns a string for the object of the class Company
                
            exemples:  
            >>>str(Company1)
            'Company name: MCGILL\nlocation: MONTREAL'
            
            >>>str(Company2)
            'Company name: MyCompany\nlocation: Laval'
            
            >>>str(Company3)
            'Company name: Plombing\nlocation: 1234 Dudemaine,Montreal'
       """
        
        return"Company Name: " + self.name + "\nLocation: " + self.location
        
        
class JobOffer:
    
    """
    A class for each job offer one can have
    
        Instance Attribues:
            ref: a refrence number for each job offer as an Integer
            title: The title of the job offer as a String
            description: The description of the job as a String
            company: An object of the previously defined class Company 
            contract: The type of contract as a String
            salary: The salary of the job offer as a Float
            
        Class Attribues:
            nb jobs: a number that keeps track of the number of JobOffer
            objects being created as an Integer, starting at 0
   """

    nb_jobs=0

    def __init__(self,title:str,company:Company,contract:str,salary:float,description:str):
        
        """
        Constructs all the necessary attributes for the JobOffer object.
        
            Parameters:
                title: The title of the job offer as a String
                company: An object of the previously defined class Company 
                contract: The type of contract as a String
                salary: The salary of the job offer as a Float
                description: The description of the job as a String
                
            Returns:
                NoneType
                
            exemples:  
            >>>Job1=JobOffer("MyFirstExample",Company1,"permanent",80000.89,
                             " To love apples, to love candy and to like chocolate")
            >>>Job1.title
            'MyFirstExample'
            >>>print(Job1.company)
            Company Name: MCGILL
            Location: MONTREAL
            >>>Job1.contract
            'permanent'
            >>>Job1.salary
             80000.89
            >>>Job1.description
            ' To love apples, to love candy and to like chocolate'
            
            >>>job2=JobOffer("MySecondExample",Company2,"indefinite",1,"To hate apples and candy")
            >>>job2.title
            'MySecondExample'
            >>>print(job2.company)
            Company Name: MyCompany
            Location: Laval
            >>>job2.contract
            'indefinite'
            >>>job2.salary
             1.0
            >>>job2.description
            'To hate apples and candy'
            
            >>>job3=JobOffer("MyThirdExample with it maintenance",Company3,
                             "idk",0,"computer repair and password management")

            >>>job3.title
            'MyThirdExample with it maintenance'
            >>>print(job3.company)
            Company Name: Plombing
            Location: 1234 Dudemaine,Montreal
            >>>job3.contract
            'idk'
            >>>job3.salary
             0.0

            >>>job3.description
            'computer repair and password management'
       """
        
        self.title=title
        self.company=company
        self.contract=contract
        self.salary=float(salary)
        self.description=description
        self.ref=JobOffer.nb_jobs+1
        
        JobOffer.nb_jobs+=1
        
        
    def update_description(self , new_description:str):
        
        """
        The method takes an input string and will update the instance attribute 
        description with the new description value.
        
            Parameters:
                new_description: the new descrption that will be updated to the 
                objet as a string
                
            Returns:
                Nonetype
                
            exemples:  
            >>>Job1.update_description("computer repair and password management")
            >>>Job1.description
            'computer repair and password management'
            
            >>>job2.update_description("nothing")
            >>>job2.description
            'nothing'
            
            >>>job3.update_description("To love apples and candy")
            >>>job3.description
            'To love apples and candy'
       """
        
        self.description=new_description
        
    def __str__(self):
        
        """
        Is the formating of a string for JobOffer
        
            Parameters:
                
            Returns:
                Returns a string for the object of the class JobOffer
                
            exemples:  
            >>>Jstr(Job1) 
            'Reference: 2\nTitle: MyFirstExample\nCompany Name: MCGILL
            \nLocation: MONTREAL\nContract: permanent\nDescription: 
            computer repair and password management\nSalary: 80000.89'
            
            >>>str(job2)
            'Reference: 3\nTitle: MySecondExample\nCompany Name: MyCompany
            \nLocation: Laval\nContract: indefinite\nDescription: nothing\nSalary: 1.0'
            
            >>>str(job3)
            'Reference: 4\nTitle: MyThirdExample with it maintenance\nCompany 
            Name: Plombing\nLocation: 1234 Dudemaine,Montreal\nContract: idk
            \nDescription: To love apples and candy\nSalary: 0.0'
       """
        
        return ("Reference: " + str(self.ref)+ "\nTitle: " + self.title  + 
                "\n" + str(self.company) + "\nContract: " + self.contract + 
                "\nDescription: " + self.description + "\nSalary: " + str(self.salary))
    

class Candidate:
    
    """
    A class for each candidate that is on this program
    
        Instance Attribues:
            first name: candidate first name as a String
            last name: candidate last name [String]
            open to work: A value indicating if the candidate is searching for a new
            job (0) or not (1) as an Integer
            email: the candidate email address as a String
            skills: a string listing the candidate’s skills separated by a dash ’-’
   """
    
    def __init__(self,first_name:str,last_name:str,open_to_work:int,email:str,skills:str):
        
        """
        Constructs all the necessary attributes for the Candidate object.
        
            Parameters:
                first_name: candidate first name as a String
                last_name: candidate last name [String]
                open_to_work: A value indicating if the candidate is searching for a new
                job (0) or not (1) as an Integer
                email: the candidate email address as a String
                skills: a string listing the candidate’s skills separated by a dash ’-’
                
            Returns:
                NoneType
       """
        
        self.first_name = first_name
        self.last_name = last_name
        self.open_to_work = open_to_work
        self.email = self.set_email(email)
        self.skills = skills.lower()
    
    def get_skills_list(self):
        
        """
        converts the skills attribute of a Candidate object into a list
        using the dash ’-’ as a delimiter and removes empty spaces
        for each skill item in the list. 
        
            Parameters:
                
            Returns:
                 skillList: list of skills of each one being a string
        """
            
        skillList=[]
        
        for word in self.skills.split("-"):
              skillList.append(word.strip())
    
        return skillList
   
    def set_email(self,email):
        
        """
        verifies if the email is a string if not, it will raise a TypeError.
        verifies if the string has one ’@’  and ends with ’.com’ if not, 
        raises a ValueError ’
        If the email is a valid email, the instance attribute email will be
        modified by the given input.

        
            Parameters:
                email: the input email as a string
                    
            Returns:
                raise ValueError with different messages depending on the error made
                or
                returns the email which will then be assigned to self.email
        """
        
        if isinstance(email, str)==True:
            
            if email.count("@")==1:
                sub_string=email[-3:]
                
                if sub_string=="com":
                    return email
                
                else:
                    raise ValueError ("Error in Class Candidate: Email format"
                                      "error:missing/too many @ and .com occurrences")
            else:
                raise ValueError ("Error in Class Candidate: Email format"
                                  "error:missing/too many @ and .com occurrences")
        else:
            raise TypeError ("Error in ClassCandidate: The input email should be a string")   
            
    def add_skill(self,skill:str):
        
        """
        Checks if skill is a string, if not, it will raise a TypeError message 
        If it is, it will put skill in lowercase and add it to the skills attribute

        
            Parameters:
                skill: the skill that will be added to the skill attribute as a string
                    
            Returns:
                raise TypeError ("Error in ClassCandidate: The input skill should be a string")
                or
                doesn't return 
        """
        
        if isinstance(skill,str)==True:
            
            skill=skill.lower()
            
            self.skills+=("-" + skill)
            
        else:
            raise TypeError ("Error in ClassCandidate: The input skill should be a string")

class JobNetwork:
    
    """
    A class JobNetwork that has all the candiates and job offers 
    
        Instance Attribues:
            jobs_list: a list of JobOffer objects 
            candidate list: a list of Candidates objects 

   """
    
    def __init__(self,jobs_list:list,candidate_list:list):
        
        """
        Constructs all the necessary attributes for the JobNetwork object.
        
            Parameters:
                jobs_list: a list of JobOffer objects 
                candidate list: a list of Candidates objects 
                
            Returns:
                NoneType
       """
        
        self.jobs_list=jobs_list
        self.candidate_list=candidate_list
    
    def find_job_per_ref(self,reff:int):
        
        """
        Goes through all the jobs in the jobs_listnd and returns the job object
        that has the corresponding reference that matches with the input reff.

        
            Parameters:
                reff: the reference number wanted (integer)
                
            Returns:
                job: the job object that corresponds to reff
                or
                0 if no job offers have the reference wanted
       """
        
        for job in self.jobs_list:
            
            if job.ref==reff:
                return job
            
        return 0
    
    def skills_in_job(self,candidate:Candidate):
        
        """
        Makes a dictionary with all the reference numbers as the keys and a list
        of 1 and 0 depending if the skills of the candiate are in the description
        of the job offer
        
            Parameters:
                candidate: object Candidate 
                
            Returns:
                dic: dictionnary with all the lists of 1 and 0 as values and 
                reference number of the job offer as key
       """
        
        
        skillList=candidate.get_skills_list()
        dic={}
        
        for job in self.jobs_list:
            List=[]
            
            for skill in skillList:
                
                if job.description.lower().count(skill)>=1:
                    List.append(1)
                    
                elif job.title.lower().count(skill)>=1:
                    List.append(1)
                    
                else:
                    List.append(0)
                    
            dic[job.ref]=List
            
        return dic
    
    def compute_similarity(self,candidate_list,job_list):
        
        """
        Converts two lists to numpy arrays and compute the cosine similarity 
        value between them.

            Parameters:
                candidate_list: a list of ones where its size is the same as the number
                                of the candidate’s skills
                job_list: a list of 0 or 1 indicating whether the candidate skill appears
                          in the job’s description or title
                
            Returns:
                0 if the one of the two lists ase numpy array are full of 0
                or
                similarity: the cosine similarity value between the two lists (integer)
       """
        
        candidate_vector=np.array(candidate_list)
        job_vector=np.array(job_list)
        
        if np.count_nonzero(candidate_vector)==False:
            return 0
        
        elif np.count_nonzero(job_vector)==False:
            return 0
        
        else: 
            candidate_vector_job_vector=np.dot(candidate_vector,job_vector)
        
            norm_can=np.linalg.norm(candidate_vector)   
            
            norm_job=np.linalg.norm(job_vector)
            
            similarity=(candidate_vector_job_vector)/(norm_can*norm_job)
            
            return similarity
        
    def compute_similarity_all(self,candidate:Candidate):
        
       """
        Creates a list of ones where its size is the same as the number
        of skills of the candidate and makes a makes a dictionary where the 
        job reference number is the key and the similarity value is the value

            Parameters:
                candidate: object Candidate 
                
            Returns:
                skill_job:the dictionary of the reference number of the job offers
                as key and the similarity value as value
       """
        
       C_list=[]
       skillList=candidate.get_skills_list()
       
       for skill in skillList:
           C_list.append(1)
           
       skill_job=self.skills_in_job(candidate) 
       
       for job in skill_job:
           
           J_list=skill_job.get(job)
           
           similarity=self.compute_similarity(C_list,J_list)
           
           skill_job[job]=similarity
       
       return skill_job
   
    def recommend_job(self,candidate:Candidate):
        
        """
        Calls compute_similarity all and finds the job reference with the highest 
        cosine similarity value. If the candidate is not open to work it return the value 0

             Parameters:
                 candidate: object Candidate 
                 
             Returns:
                 max_nb: the job reference with the highest similarity value (integer)
                 or
                 0 is the candiate is not open to work (open to work attribute is not 0)
        """
        
        if candidate.open_to_work==0:
            
            skill_job=self.compute_similarity_all(candidate)
            
            max_nb=max(skill_job,key=skill_job.get)
            
            return max_nb
        
        else:
            return 0
        
    def print_recommended_job(self,candidate:Candidate):
        
        """
        Calls recommend_job to get the reference number of the recommended job 
        to the candidate and find the job with that ref to print it . 

             Parameters:
                 candidate: object Candidate 
                 
             Returns:
        """
        
        recommendation=self.recommend_job(candidate)
        
        if recommendation>=1:
            
            job=self.find_job_per_ref(recommendation)
            
            print(job)
            
        elif recommendation==0:
            
            print("This candidate is not looking for a job")
           
           
       

    
    
   
    
    
    
    
    
    
    
    
    
    
    
    