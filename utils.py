import openai
import requests

def fetchjob(job_id):
    url_job = 'https://bepc.backnetwork.net/JobSiftBeta/assets/php/equalizer.php'
    data_job = {"job": job_id, "get_description": "1"}
    response_job = requests.post(url_job, data=data_job)
    job_description = response_job.text
    return job_description


def equalize(job_description):
    #Equalize Job Description
    score_summary = openai.ChatCompletion.create(
    model= "gpt-4",
    messages=[
        {"role":"user", "content":"You are an expert recruiting AI, specialized in Diversity, Equity, and Inclusion, \
         and guided by scientific studies such as 'Evidence That Gendered Wording in Job Advertisements Exists and\
         Sustains Gender Inequality'. Your task is to revise the following job description\
         to make it more inclusive, not just in terms of gender but also considering age, ethnicity, and disability biases.\
         Your Job is to revise a Job Description and make it more inclusive.\
         The study suggests that masculine wording in job advertisements may cue women to the possibility\
         that they do not belong in that occupation, which in turn may make the job less appealing to women.\
         They also find that masculine wording does indeed make jobs less appealing to women, even when the occupations\
         are not traditionally male-dominated.\
         Guidelines:\
         This is very important!: Maintain the original meaning and intent of the job description. Do not invent any new requirements.\
         Understand that this task has legal implications, requiring utmost accuracy and sensitivity.\
         To make a job description that is not gender biased, you should avoid using masculine or feminine words.\
         Instead, use gender-neutral language. For example, instead of saying 'he' or 'she',\
         you could say 'they' or 'the individual'. You should also avoid using words that are associated with one\
         gender or the other, such as 'strong' or 'nurturing'.\
         Here are some specific words that need to be replaced:\
         Strong -> capable\
         Nurturing -> supportive\
         Leader -> manager\
         Boss -> supervisor\
         Man -> person\
         Woman -> person\
         In addition to avoiding gendered words, you should also pay attention to the overall tone of your job description.\
         Make sure that it is welcoming and inclusive, and that it does not make assumptions about the gender of the ideal candidate.\
         Here are some tips for writing a gender-neutral job description:\
         Use active voice instead of passive voice.\
         Avoid using gendered pronouns.\
         Use job-related terms instead of gender-specific terms.\
         Avoid using stereotypes.\
         Make sure that the job description is welcoming and inclusive.\
         By following these tips, you can write a job description that is not gender biased and that will appeal to a wider range of candidates."},

        {"role":"user", "content":f"Job Description: {job_description}"},
        {"role":"user", "content":f"By adhering to these guidelines, create a job description that is welcoming to a diverse\
        range of candidates without making assumptions about their gender, age, ethnicity, or abilities. The output should only be\
         The new Job description, do not add 'Job Description is:' or anything like that."},
        ],
        temperature=0.3,
        )
    new_job_description = score_summary['choices'][0]['message']['content']
    return new_job_description