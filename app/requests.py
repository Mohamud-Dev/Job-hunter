import urllib.request,json
from .models import Jobs,Hiring

base_url=None


def configure_request(app):
    global base_url
    base_url = app.config["BASE_URL"]

	

def get_jobs(category):
    '''
    Function that gets the json response to our url request
    '''
    get_jobs_url = base_url.format(category)

    with urllib.request.urlopen(base_url) as url:
        get_jobs_data = url.read()
        get_jobs_response = json.loads(get_jobs_data)

        jobs_results = None

       
       
        jobs_results = process_jobs(get_jobs_response)


    return jobs_results



def process_jobs(jobs_list):
	'''
	'''
	jobs_object = []
	for job_item in jobs_list:
		id = job_item.get('id')
		title = job_item.get('title')
		company = job_item.get('company')
		url = job_item.get('url')
		location = job_item.get('location')
		description = job_item.get('description')
		
		
		jobs_result = Jobs(id,title,company,url,location,description,description)
		jobs_object.append(jobs_result)	
		
	return jobs_object

def search_jobs(query):
    
    search_jobs_url = 'https://jobs.github.com/positions.json?description={}'.format(query)
    with urllib.request.urlopen(search_jobs_url) as url:
        search_jobs_data = url.read()
        search_jobs_response = json.loads(search_jobs_data)

        search_jobs_results = None

        
        
        search_jobs_results = process_jobs(search_jobs_response)


    return search_jobs_results