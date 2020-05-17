def verkadaIPAddressFinder(str):
    # Note that alphabatical is just important to know that '.' comes before numbers
    def go_through_all_cases():
        distinct_ip_addresses = []
        # place all three periods and then check if it's legal
        for p_one in range(1, len(str) - 2):
            for p_two in range(p_one + 1, len(str) - 1):
                for p_three in range(p_two + 1, len(str)):
                    print(f'p_one: {p_one}, p_two: {p_two}, p_three: {p_three}')
                    s1_num = str[0:p_one]
                    s2_num = str[p_one:p_two]
                    s3_num = str[p_two:p_three]
                    s4_num = str[p_three:len(str)]

                    if s3_num == '80':
                        print('stuff')

                    # check that all four string splits are at max 3 long
                    if len(s1_num) > 3 or len(s2_num) > 3 or len(
                            s3_num) > 3 or len(s4_num) > 3:
                        pass
                    #
                    # # check that the string split does not have leading zeros
                    #
                    # if (len(s1_num) > 1 and s1_num[0] == '0') or (
                    #         len(s2_num) > 1 and s2_num[0] == '0') or (
                    #         len(s3_num) > 1
                    #         and s3_num[0] == '0') or (len(s4_num) > 1
                    #                                   and s4_num[0] == '0'):
                    #     print(f's1_num: {(s1_num)}')
                    #     print(f's2_num: {(s2_num)}')
                    #     print(f's3_num: {(s3_num)}')
                    #     print(f's4_num: {(s4_num)}\n')
                    #     break
                    #
                    # # now check they each string split is a number between 0 and 255
                    # if int(s1_num) in range(0, 256) and int(
                    #         s2_num) in range(0, 256) and int(
                    #     s3_num) in range(0, 256) and int(
                    #     s4_num) in range(0, 256):
                    #     ip_address = s1_num + '.' + s2_num + '.' + s3_num + '.' + s4_num
                    #     distinct_ip_addresses.append(ip_address)
        return distinct_ip_addresses

    return go_through_all_cases()


if __name__ == "__main__":
    print(verkadaIPAddressFinder('19212800'))


