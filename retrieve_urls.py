def retrieve_urls(url, extra_pages=0):
    # example https://webpage/0001.html
    # backtrack from the end
    # first is possibile of .pdf .html .sth
    # cast to str

    url = str(url)
    url_list = [url]
    # extra pages apart from url given, meaning a pattern has to be found
    if extra_pages == 0:
        return url_list
    elif extra_pages > 0:
        i = len(url)-1
        while i >=0 and url[i] != '.':
            i-=1
        
        # either found . or its 0

        if i >1:
            # found the thing before the dot 
            extracted_end = url[:i]
        else:
            #differne pattern