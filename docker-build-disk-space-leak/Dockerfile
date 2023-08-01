FROM alpine:3.18.2 AS base1
RUN echo test1 > test1
RUN echo test2 > test2
WORKDIR /app


FROM base1 AS internal1
WORKDIR /app
COPY lockfile.txt ./lock1.txt
RUN echo test3 > test3


FROM base1 AS target2
WORKDIR /app
RUN echo test4 > test4


FROM internal1 AS internal2
RUN echo test5 > test5


FROM alpine:3.18.2 AS base2
RUN echo test6 > test6
RUN echo test7 > test7
WORKDIR /app
COPY lockfile.txt ./lock2.txt
RUN echo test8 > test8


FROM base2 AS target1
RUN echo test9 > test9
COPY . /app/


FROM base2 AS internal3
COPY . /app/
COPY --from=internal2 /app/ .
RUN echo test10 > test10
RUN echo test11 > test11

FROM internal3 AS target4
CMD echo target4

FROM internal3 AS target3
CMD echo target3
