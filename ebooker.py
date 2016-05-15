# main python file for the tool ebooker
import sys
import urllib2
# Book Search
#
# Request
#
# /search/{query}	Search query (Note: 50 characters maximum)
# Example: /search/php mysql
#
# /search/{query}/page/{number}
# optional	The page number of results (Note: 10 results per page)
# Example: /search/php mysql/page/3

# Response
#
# Error	Error code / description (Note: request success code = 0)
# Time	Request query execution time (seconds)
# Total	The total search results
# Page	The page number of results (Note: limit = 10 results on page)
# Books	Search results
# Array: ID, Title, SubTitle (optional), Description, Image


#some constant value
ebook_website = "http://it-ebooks-api.info//v1"
search_request_query = "/search/"
search_request_page = "/page/"



# the main function
def main(argv):
    print_help(argv)
    handle_search()

# print the help message
def print_help(argv):
    print "\n"
    print "---------------------------------------------------------------------------------------------------"
    print "welcome to use the ebooker tools, with this tools you can search, download and managment your ebook"
    print "---------------------------------------------------------------------------------------------------"

# handle for search
def handle_search():
    print "Please input your keyword for search ..."
    keyword = raw_input("keyword:")
    print "the keyword you input is :" + keyword
    print "start search on the ebook website ..."
    start_search(keyword)


def start_search(keyword):
    print "start search : " + keyword

    url = ebook_website + search_request_query + keyword
    do_search(url)

def do_search(url):
    # just print the searching url
    print "dp search : " + url
    response = urllib2.urlopen(url)
    content = response.read()
    # here the cotent is the response search list
    # print content
    parse_search_content(content)

def parse_search_content(content):
    print "parse search content"


if __name__=="__main__":
    main(sys.argv)