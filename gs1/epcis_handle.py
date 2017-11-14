import requests

queryURL = 'http://gs1ap.asuscomm.com:8447/epcis/Service/Poll/SimpleEventQuery?'
dataFormat = 'format=JSON&' # format=XML&

captureURL = 'http://gs1ap.asuscomm.com:8447/epcis/Service/EventCapture'
captureHeader = {'Content-Type': 'application/xml; charset=utf-8'}


def main():
    # response = requests.get(queryURL + dataFormat)
    # print(response.text)

    f = open("sampleData.txt", 'r')
    sampleData = f.read()
    # print(sampleData)
    f.close()

    response = requests.post(captureURL, headers=captureHeader, data=sampleData)
    print(response.text)

if __name__ == '__main__':
    main()