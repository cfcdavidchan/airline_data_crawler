import requests, os, shutil, json
import subprocess
import time, re

root_path = os.getcwd()

airline_data_path = os.path.join(root_path,'airline_data/')
if os.path.exists(airline_data_path):
    shutil.rmtree(airline_data_path)
else:
    os.makedirs(airline_data_path)

airline_data = dict()

airline_data['Alaska_Airlines'] = 'https://www.tripadvisor.com/Airline_Review-d8729017-Reviews-Alaska-Airlines'
airline_data['Southwest_Airlines'] = 'https://www.tripadvisor.com/Airline_Review-d8729156-Reviews-Southwest-Airlines'
airline_data['Delta_Air_Lines'] = 'https://www.tripadvisor.com/Airline_Review-d8729060-Reviews-Delta-Air-Lines'
airline_data['United_Airlines'] = 'https://www.tripadvisor.com/Airline_Review-d8729177-Reviews-United-Airlines'
airline_data['Frontier_Airlines'] = 'https://www.tripadvisor.com/Airline_Review-d8729213-Reviews-Frontier-Airlines'
airline_data['American_Airlines'] = 'https://www.tripadvisor.com/Airline_Review-d8729020-Reviews-American-Airlines'
airline_data['Spirit_Airlines'] = 'https://www.tripadvisor.com/Airline_Review-d8729157-Reviews-Spirit-Airlines'
airline_data['JetBlue'] = 'https://www.tripadvisor.com/Airline_Review-d8729099-Reviews-JetBlue'
airline_data['Hawaiian_Airlines'] = 'https://www.tripadvisor.com/Airline_Review-d8729086-Reviews-Hawaiian-Airlines'
airline_data['Allegiant_Air'] = 'https://www.tripadvisor.com/Airline_Review-d8729019-Reviews-Allegiant-Air'




#virtual environment command
virtual = 'source activate tripadvisor'

# crawler path
path_crawler = os.path.join(root_path,'tripadvisor_crawler/')
#path_crawler = '/home/david/coding/tripadvisor/tripadvisor_crawler'

problem_url = dict()
timer = dict()

for name, url in airline_data.items():
    start = time.time()
    print('crawling %s' % name)
    # crawler command
    commnad = 'scrapy crawl tripadvisor_airline -a start_url="%s" -a name="%s"' % (url, name)
    try:
        subprocess.Popen('%s && %s' % (virtual, commnad), shell=True, cwd=path_crawler,
                         executable="/bin/bash").wait()
    except:
        problem_url[name] = url
    end = time.time()

    try:
        airline_name = re.sub(r"[^A-Za-z]+", '', name)
        csv_name = '%s_all_data.csv' % airline_name
        csv_path = 'airline_data/%s/%s' % (airline_name, csv_name)
        with open(csv_path) as f:
            review_number = sum(1 for line in f) -1
        timer[name] = [end-start, review_number]
    except:
        pass


with open('problem_url.json', 'w') as fp:
    json.dump(problem_url, fp)

with open('timer.json', 'w') as fp:
    json.dump(timer, fp)
