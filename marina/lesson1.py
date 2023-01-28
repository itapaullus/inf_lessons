h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))
h3, m3 = map(int, input().split(':'))
h4, m4 = map(int, input().split(':'))

if h2 < h1:
    h2 = h2 + 24

if h4 < h3:
    h4 = h4 + 24

flight1 = h2*60+m2 - h1*60-m1
flight2 = h4*60+m4 - h3*60-m3

minute_ans = (flight1+flight2)/2

print(f'{round(minute_ans//60):02}:{round(minute_ans%60):02}')
