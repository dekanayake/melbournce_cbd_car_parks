from hashlib import sha1
import hmac
import binascii
def getUrl(request):
    devId = 3000964
    key = '6b4b24cf-0758-430b-a077-3351a14bdba5'
    request = request + ('&' if ('?' in request) else '?')
    raw = request+'devid={0}'.format(devId)
    hashed = hmac.new(key, raw, sha1)
    signature = hashed.hexdigest()
    return 'http://timetableapi.ptv.vic.gov.au'+raw+'&signature={1}'.format(devId, signature)
print('Enter request:')
request = raw_input()
print getUrl(request)
