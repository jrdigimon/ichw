def main():
    '''Module for currency exchange

    This module provides several string parsing functions to implement a 
    simple currency exchange routine using an online currency service. 
    The primary function in this module is exchange.'''
    def before_space(s):
        '''Returns: Substring of s; up to, but not including, the first space
           Parameter s: the string to slice
           Precondition: s has at least one space in it'''
        t = s.split(' ',maxsplit = 1)
        return t[0]
    def test_before_space():
        '''Test the before_space function.'''
        assert(before_space('0.8963 Euros') == '0.8963')
        assert(before_space(' 0.6983 Euros') == '')
        assert(before_space('ab cd') == 'ab')
    test_before_space()
    def after_space(s):
        '''Returns: Substring of s after the first space
           Parameter s: the string to slice
           Precondition: s has at least one space in it'''
        t = s.split(' ',maxsplit = 1)
        return t[1]
    def test_after_space():
        '''Test the after_space function'''
        assert(after_space('0.8963 Euros') == 'Euros')
        assert(after_space('0.8963 Euros is convertable') == 'Euros is convertable')
        assert(after_space(' Can this pass?') == 'Can this pass?')
    test_after_space()
    def first_inside_quotes(s):
        '''Returns: The first substring of s between two (double) quote characters
           Parameter s: a string to search
           Precondition: s is a string with at least two (double) quote characters inside.'''
        t = s.split('"')
        return t[1]
    def test_first_inside_quotes():
        '''Test the first_inside_quotes function.'''
        assert(first_inside_quotes('A "B C" D') == 'B C')
        assert(first_inside_quotes('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}') == 'from')
        assert(first_inside_quotes('This assignment is "interesting"') == 'interesting')
    test_first_inside_quotes()
    def get_from(json):
        '''Returns: The FROM value in the response to a currency query.
           Parameter json: a json string to parse
           Precondition: json is the response to a currency query'''
        t = json.split('"from"')
        use = t[1]
        re = first_inside_quotes(use)
        return re
    def test_get_from():
        '''Test the get_from function.'''
        json1 = '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
        assert(get_from(json1) == '2 United States Dollars')
        json2 =  '{"from":"","to":"","success":false,"error":"Source currency code is invalid."}'
        assert(get_from(json2) == '')
        json3 = '{ "from" : "2.5 Chinese Yuan", "to" : "0.31507457567753 Euros", "success" : true, "error" : "" }'
        assert(get_from(json3) == '2.5 Chinese Yuan')
    test_get_from()
    def get_to(json):
        '''Returns: The TO value in the response to a currency query.
           Parameter json: a json string to parse
           Precondition: json is the response to a currency query'''
        t = json.split('"to"')
        use = t[1]
        re = first_inside_quotes(use)
        return re
    def test_get_to():
        '''Test the get_to function.'''
        json1 = '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
        assert(get_to(json1) ==  '1.825936 Euros')
        json2 = '{"from":"","to":"","success":false,"error":"Source currency code is invalid."}'
        assert(get_to(json2) == '')
        json3 = '{ "from" : "2.5 Chinese Yuan", "to" : "0.31507457567753 Euros", "success" : true, "error" : "" }'
        assert(get_to(json3) == '0.31507457567753 Euros')
    test_get_to()
    def has_error(json):
        '''Returns: True if the query has an error; False otherwise.
           Parameter json: a json string to parse
           Precondition: json is the response to a currency query'''
        t = json.split('"error"')
        use = t[1]
        if use == ':""}':
            return False
        else:
            return True
    def test_has_error():
        json1 =  '{"from":"","to":"","success":false,"error":"Source currency code is invalid."}'
        assert(has_error(json1) == True)
        json2 = '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
        assert(has_error(json2) == False)
        json3 = '{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }'
        assert(has_error(json3) == True)
    test_has_error()
    def currency_response(currency_from, currency_to, amount_from):
        '''Returns: a JSON string that is a response to a currency query.
           Parameter currency_from: the currency on hand
           Precondition: currency_from is a string
    
           Parameter currency_to: the currency to convert to
           Precondition: currency_to is a string
    
           Parameter amount_from: amount of currency to convert
           Precondition: amount_from is a float'''
        from urllib.request import urlopen
        doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={}'.format(currency_from,currency_to,amount_from))
        docstr = doc.read()
        doc.close()
        json = docstr.decode('ascii')
        return json
    def test_currency_response():
        '''Test the currency_response function.'''
        assert(currency_response('USD','EUR',2.5) == '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')
        assert(currency_response('usd','EUR',2.5) == '{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')
        assert(currency_response('USD','EUR','joking') == '{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }')
    test_currency_response()
    def iscurrency(currency):
        '''Returns: True if currency is a valid currency. False otherwise.
           Parameter currency: the currency code to verify
           Precondition: currency is a string.'''
        if currency in ['AED','AFN','ALL','AMD','ANG','AOA','ARS','AUD','AWG','AZN',
                        'BAM','BBD','BDT','BGN','BHD','BIF','BMD','BND','BOB','BRL',
                        'BSD','BTC','BTN','BWP','BYR','BZD','CAD','CDF','CHF','CLF',
                        'CLP','CNY','COP','CRC','CUC','CUP','CVE','CZK','DJF','DKK',
                        'DOP','DZD','EEK','EGP','ERN','ETB','EUR','FJD','FKP','GBP',
                        'GEL','GGP','GHS','GIP','GMD','GNF','GTQ','GYD','HKD','HNL',
                        'HRK','HTG','HUF','IDR','ILS','IMP','INR','IQD','IRR','ISK',
                        'JEP','JMD','JOD','JPY','KES','KGS','KHR','KMF','KPW','KRW',
                        'KWD','KYD','KZT','LAK','LBP','LKR','LRD','LSL','LTL','LVL',
                        'LYD','MAD','MDL','MGA','MKD','MMK','MNT','MOP','MRO','MTL',
                        'MUR','MVR','MWK','MXN','MYR','MZN','NAD','NGN','NIO','NOK',
                        'NPR','NZD','OMR','PAB','PEN','PGK','PHP','PKR','PLN','PYG',
                        'QAR','RON','RSD','RUB','RWF','SAR','SBD','SCR','SDG','SEK',
                        'SGD','SHP','SLL','SOS','SRD','STD','SVC','SYP','SZL','THB',
                        'TJS','TMT','TND','TOP','TRY','TTD','TWD','TZS','UAH','UGX',
                        'USD','UYU','UZS','VEF','VND','VUV','WST','XAF','XAG','XAU',
                        'XCD','XDR','XOF','XPD','XPF','XPT','YER','ZAR','ZMK','ZMW',
                        'ZWL']:
            return True
        else:
            return False
    def test_iscurrency():
        '''Test the iscurrency function'''
        assert(iscurrency('CNY') == True)
        assert(iscurrency('China Yuan') == False)
        assert(iscurrency('cny') == False)
    test_iscurrency()
    def exchange(currency_from, currency_to, amount_from):
        '''Returns: amount of currency received in the given exchange.
           Parameter currency_from: the currency on hand
           Precondition: currency_from is a string for a valid currency code
           Parameter currency_to: the currency to convert to
           Precondition: currency_to is a string for a valid currency code
           Parameter amount_from: amount of currency to convert
           Precondition: amount_from is a float'''
        text = currency_response(currency_from, currency_to, amount_from)
        temp1 = get_to(text)
        temp2 = temp1.split()
        amount_to = float(temp2[0])
        return amount_to
    def test_exchange():
        '''Test the exchnge function.'''
        assert(exchange('USD','EUR',2.5) == 2.1589225)
        assert(exchange('TOP','TTD',6) == 17.511635818151)
        assert(exchange('XPD','ZWL',0.3) == 94963.915451466)
    test_exchange()
    print('All tests passed.')
if __name__ == "__main__":
    main()
