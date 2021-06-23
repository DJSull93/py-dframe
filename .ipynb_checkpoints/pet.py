import pandas as pd
import numpy as np
import random
import string
np.random.seed(56)
from icecream import ic

if __name__ == '__main__':
    menu = input('press number'
                 '2. 판다스 버전 출력\n'
                 '3. 판다스 라이브러리 버전 정보 모두 출력\n'
                 '4. 주어진 값으로 DataFrame 객체를 생성하시오\n'
                 '5. 객체내부 정보를 출력\n'
                 '6. 객체 상위 3열까지 출력\n'
                 '7. animal과 age 컬럼만 출력\n'
                 '8. 객체의 3, 4, 8번 행에 해당하는 animal과 age 값만 출력\n'
                 '9. visit 컬럼에서 3 초과하는 값 출력\n'
                 '10. age 에서 NaN 값 출력\n'
                 '11. age가 3살 미만 고양이값 출력\n'
                 '12. age가 2살이상 4살 미만인 값 출력\n'
                 '13. f 행의 나이를 1.5살로 변경\n'
                 '14. 객체에서 visit 의 합 출력\n'
                 '15. 동물별로 나이의 평균 출력\n'
                 '16. k행을 추가하여 dog , 5.5세, 방문회수 2회, 우선권없음(no) 열을 추가\n'
                 '16-1. 방금 추가한 열 삭제\n'
                 '17. 객체에 있는 동물의 종류의 수 출력\n'
                 '18. age 는 내림차순, visits 는 오름차순으로 정렬\n'
                 '19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력\n'
                 '20. snake 를 python 으로 값을 변경\n'
                 '21. 각각의 동물 유형과 방문 횟수에 대해 평균나이를 찾으시오. 즉,각 행은 animal 이고, 각 열은 visits 이며, 값은 평균연령 (힌트, 피벗 테이블을 활용해야 함)\n'
                 '22. 다음 객체에서 키값 A와 중복된 값이 제거된 1,2,3,4,5,6,7 이 출려되는 코드를 작성\n'
                 '23. 다음 객체에서 행의 각 요소에서 행의 평균을 뺀 값을 출력\n'
                 '24. 다음 객체에서 가장 작은 합계를 가진 숫자열의 열을 출력\n'
                 '25. 다음 객체에서 중복된 값이 없는 유니크한 열의 카운트 출력(중복되지 않은 행은 몇 개..)\n'
                 '26. 객체의 각 행에 대해 세번째 NaN 값이 들어 있는 열을 찾으시오. 일련의 열 레이블을 반환해야 합니다. 답은 e, c, d, h, d 입니다.\n'
                 '27. 다음 객체에서 grps 에서 a, b, c 별로 가장 큰 값을 찾으시오.\n'
                 '28 다음 객체를 list 로 변환하시오\n'
                 '29 다음 객체를 dictionary 로 변환하시오\n'
                 '30 다음 객체를 customer_id 를 인덱스로하고 product_code 를 컬럼으로, purchare_amount 를 값으로, 재구성하시오\n'
                 '31 30번 객체를 customer_id 와 grade 를 인덱스로하고 product_code 를 컬럼으로, purchare_amount 를 값으로, 재구성하시오\n'
                 )

    def quiz_2():
        pass

    def quiz_3():
        pass

    def quiz_4():
        pass

    def quiz_5():
        pass

    def quiz_6():
        pass

    def quiz_7():
        pass

    def quiz_8():
        pass

    def quiz_9():
        pass

    def quiz_10():
        pass

    def quiz_11():
        pass

    def quiz_12():
        pass

    def quiz_13():
        pass

    def quiz_14():
        pass

    def quiz_15():
        pass

    def quiz_16():
        pass

    def quiz_17():
        pass

    def quiz_18():
        pass

    def quiz_19():
        pass

    def quiz_20():
        pass

    def quiz_21():
        pass

    def quiz_22():
        pass

    def quiz_23():
        pass

    def quiz_24():
        pass

    def quiz_25():
        pass

    def quiz_26():
        pass

    def quiz_27():
        pass

    def quiz_28():
        pass

    def quiz_29():
        pass

    def quiz_30():
        pass

    def quiz_31():
        pass

    while 1:
        select = input('menu')
        if select == '0': break
        elif select == '2': quiz_2()
        elif select == '3': quiz_3()
        elif select == '4': quiz_4()
        elif select == '5': quiz_5()
        elif select == '6': quiz_6()
        elif select == '7': quiz_7()
        elif select == '8': quiz_8()
        elif select == '9': quiz_9()
        elif select == '10': quiz_10()
        elif select == '11': quiz_11()
        elif select == '12': quiz_12()
        elif select == '13': quiz_13()
        elif select == '14': quiz_14()
        elif select == '15': quiz_15()
        elif select == '16': quiz_16()
        elif select == '17': quiz_17()
        elif select == '18': quiz_18()
        elif select == '19': quiz_19()
        elif select == '20': quiz_20()
        elif select == '21': quiz_21()
        elif select == '22': quiz_22()
        elif select == '23': quiz_23()
        elif select == '24': quiz_24()
        elif select == '25': quiz_25()
        elif select == '26': quiz_26()
        elif select == '27': quiz_27()
        elif select == '28': quiz_28()
        elif select == '29': quiz_29()
        elif select == '30': quiz_30()
        elif select == '31': quiz_31()
        else: continue

def pandas_version_output():
    # pandas 버젼 출력
    print("pandas version: ", pd.__version__)

    # %%

    # pandas 라이브러리 버전 정보 모두 출력하기
    pd.show_versions(as_json=False)

    # %%

    data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
            'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
            'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    # %%

    # DF 생성
    df = pd.DataFrame(data,
                      index=labels)

    # %%

    # 객체 내부 정보 출력
    df

    # %%

    # 객체 상위 3열 출력
    df.head(3)

    # %%

    # animal, age 칼럼만 출력
    df.iloc[:, 0:2]

    # %%

    # 객체 3, 4, 8 행 해당 animal, age 출력
    df.iloc[[2, 3, 7]]

    # %%

    # visit 컬럼에서 3초과 값 출력
    df[df['visits'] >= 3]

    # %%

    # age nan 출력
    df[df['age'].isnull()]

    # %%

    # 3살 미만 고양이 출력
    df[(df['animal'] == 'cat') & (df['age'] < 3)]

    # %%

    # 2살 이상 4살 미만 값 출력
    df[(df['age'] >= 2) & (df['age'] < 4)]

    # %%

    # f행 나이 1.5로 변경
    df.loc['f', 'age'] = 1.5
    df

    # %%

    # 객체 visit의 합 출력
    df['visits'].sum()

    # %%

    # 동물 나이 평균 출력
    df['age'].mean()

    # %%

    # k열 추가 dog 5.5 no 2 추가
    df.loc['k'] = ['dog', 5.5, 2, 'no']
    df

    # %%

    # 방금 추가 열 삭제
    df.drop('k', inplace=True)
    df

    # %%

    # 객체 동물 종류 수 출력
    df['animal'].value_counts()

    # %%

    # age 내림차순, visit 오름차순 정렬
    df.sort_values(by=['age', 'visits'], ascending=[False, True])

    # %%

    # priority 의 yes를 True, no 를 False  로 맵핑 후 출력
    df['priority'] = df['priority'].map({'yes': 'True', 'no': 'False'})
    df

    # %%

    # snake 를 python 으로 값을 변경
    df['animal'] = df['animal'].replace('snake', 'python')
    df

    # %%

    # 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.
    # 즉,각 행은 animal 이고, 각 열은 visit 이며, 값은 평
    df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')

    # %%

    # 22. 다음 객체에서 키값 A와 중복된 값이 제거된 1,2,3,4,5,6,7 이 출력되는 코드를 작성
    df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
    df.loc[df['A'].shift() != df['A']]

    # %%

    # 23. 다음 객체에서 행의 각 요소에서 행의 평균을 뺀 값을 출력
    df = pd.DataFrame(np.random.random(size=(5, 3)))
    df.sub(df.mean(axis=1), axis=0)

    # %%

    # 24. 다음 객체에서 가장 작은 합계를 가진 숫자열의 열을 출력
    df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
    df.sum().idxmin()

    # %%

    # 25. 다음 객체에서 중복된 값이 없는 유니크한 열의 카운트 출력(중복되지 않은 행은 몇 개..)
    df = pd.DataFrame(np.random.randint(0, 2, size=(10, 3)))
    sd = df.duplicated(keep=False) == False
    print(sd)
    print(sum(sd))

    # %%

    # 26. 객체의 각 행에 대해 세번째 NaN 값이 들어 있는 열을 찾으시오. 일련의 열 레이블을 반환해야 합니다.
    # 답은 e, c, d, h, d 입니다.
    nan = np.nan
    data = [[0.04, nan, nan, 0.25, nan, 0.43, 0.71, 0.51, nan, nan],
            [nan, nan, nan, 0.04, 0.76, nan, nan, 0.67, 0.76, 0.16],
            [nan, nan, 0.5, nan, 0.31, 0.4, nan, nan, 0.24, 0.01],
            [0.49, nan, nan, 0.62, 0.73, 0.26, 0.85, nan, nan, nan],
            [nan, nan, 0.41, nan, 0.05, nan, 0.61, nan, 0.48, 0.68]]
    columns = list('abcdefghij')
    df = pd.DataFrame(data, columns=columns)
    (df.isnull().cumsum(axis=1) == 3).idxmax(axis=1)

    # %%

    # 27. 다음 객체에서 grps 에서 a, b, c 별로 가장 큰 값을 찾으시오.
    # 출력 결과는
    #  grps
    #   a    409
    #   b    156
    #   c    345
    # 이렇게 나옵니다.
    df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                       'vals': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
    df.pivot_table(index='grps', values='vals', aggfunc='max')

    # %%

    # 28 다음 객체를 list 로 변환하시오
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df.columns.values.tolist() + df.values.tolist()

    # %%

    # 29 다음 객체를 dictionary 로 변환하시오
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df.to_dict()

    # %%

    # 30 다음 객체를 customer_id 를 인덱스로하고 product_code 를 컬럼으로, purchare_amount 를 값으로, 재구성하시오
    df = pd.DataFrame({"customer_id": ['kim', 'lee', 'park', 'song', 'yoon', 'kang', 'tak', 'ryu', 'jang'],
                       "product_code": ['com', 'phone', 'tv', 'com', 'phone', 'tv', 'com', 'phone', 'tv'],
                       "grade": ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
                       "purchase_amount": [30, 10, 0, 40, 15, 30, 0, 0, 10]})
    df

    # %%

    # 31 30번 객체를
    #    customer_id 와 grade 를 인덱스로하고 product_code 를 컬럼으로,
    #    purchare_amount 를 값으로, 재구성하시오

    # %%