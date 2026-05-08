def retrieve_urls(url, extra_pages=0):
    # Objective: Returns a list of urls, given one initial and finds a pattern to obtain the next ones (with a set extra pages)
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
            after = url[i:]
            # found the thing before the dot 
            extracted_end = url[:i]
            a = len(extracted_end)-1
            digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            while extracted_end[a] in digits:
                a -=1
            pattern =  int(extracted_end[(a+1):])
            before = extracted_end[:(a+1)]
            num = 0
            pattern +=1 
            # pattern +1 as url_list already has the default one 
            # make all the urls with the pattern
            while num < extra_pages:
                url_list.append(before+str(pattern)+after)
                num +=1
                pattern +=1
        return url_list
            #differne pattern