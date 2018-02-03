# -*- coding: utf-8 -*-


def sum_of_list(list_data):

    result = 0
    for i in list_data:
        result += i


    return result


def merge_and_sort(list_data_a, list_data_b):
    result = list_data_a + list_data_b


    # ==================================
    return result.sort()


def delete_a_list_element(list_data, element_value):
    list_data2 = []
    for a in list_data:
        if(a == element_value):
            continue
        list_data2.append(a)

    result = list_data2

    # ==================================
    return result


def comparison_list_size(list_data_a, list_data_b):
    result = list_data_a if len(list_data_a) > len(list_data_b) else list_data_b

    # ==================================
    return result


def odd_even_check(a, b):

    result = "Even" if ((a+b) % 2) == 0 else "Odd"

    # ==================================
    return result


def discount_price(price):
    # '''
    # Input:
    #   - price : 숫자형 값
    # Output:
    #   - price의 값이 100,000 미만일 경우 10% 할인된 값이 반환,
    #     10만원 이상일 경우 20퍼센트 할인된 값이 반환됨
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> gwf.discount_price(40000)
    #   36000.0
    #   >>> gwf.discount_price(110000)
    #   880000.0
    # '''
    # pass
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def find_smallest_value(list_data):
    # '''
    # Input:
    #   - list_data : 숫자형 값으로 이루어진 list
    # Output:
    #   - list_data의 element중 가장 작은 값이 반환됨
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> a = [1, 2, 3, 4, 5]
    #   >>> gwf.find_smallest_value(a)
    #   1
    #   >>> a = [5, 4, 3, 0, 100, 200]
    #   >>> gwf.find_smallest_value(a)
    #   0
    # '''
    # pass
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def binary_converter(decimal_number):
    result = ""
    while (decimal_number > 0) :
        reminder = decimal_number % 2
        decimal_number = int(decimal_number / 2)
        result = str(reminder) + result
        print(result)

    # ==================================
    return result


def number_of_cases(list_data):
    # '''
    # Input:
    #   - list_data : 숫자 또는 문자 값으로 이루어진 list
    # Output:
    #   - list_data 안에 있는 element 조합의 모든 경우의 수,
    #     ※ 반환되는 list에는 문자열 Type만 들어 있으며
    #        list_data 안에 숫자형 값이 있을 경우 문자열로 변환하여 처리
    #     ※ 중복되는 값은 삭제된 후 반환 되어야 함
    #     ※ 최종결과는 Sorting된 후에 반환되어야 함
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> a = ['a', 'b', 'c']
    #   >>> gwf.number_of_cases(a)
    #   ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
    #   >>> a = ['a', 'a']
    #   >>> gwf.number_of_cases(a)
    #   ['aa']
    #   >>> a = [1, 2, 3, 'a']
    #   >>> gwf.number_of_cases(a)
    #   ['11', '12', '13', '1a', '21', '22', '23', '2a', '31', '32', '33', '3a', 'a1', 'a2', 'a3', 'aa']
    # '''
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def main():
    # ===Test your functions=============
    # 아래 "pass" 부분을 삭제한 후 테스트하고
    # 싶은 코드를 자유롭게 작성하시오
    # pass
    # binary_converter(10)
    # sum_of_list([1,2,3])
    # print(odd_even_check(1,2))
    # print(delete_a_list_element([1,2,3], 2))
    # print(merge_and_sort([1,3], [2,4]))
    print(comparison_list_size([1,2], [2,3,4]))

    # ==================================

if __name__ == "__main__":
    main()
