#Specifying the base image name - FROM command is mandatory

FROM python:alpine

RUN apk update
RUN apk add git
RUN apk add curl

RUN touch abc.py
RUN echo -e 'print("Executed Python Script: ")\nprint("In a Docker Container: ")' > abc.py 

CMD ["python", "abc.py"]





# Below will only work in -it mode -> docker container run -it <image-id/name>
#
# echo -e 'a=int(input("1st no.: "))\nb=int(input("2nd no.: "))\nc=a*b\nprint("line-1--", c)\nprint("line-2")\nprint("line-3")' > aaa.py
#