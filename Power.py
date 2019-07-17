class Var:
    number = int(input('Enter the number here: '))

    def __init__(self, number):
        number = self, number
        return number
    # def numb(self, n):
    #     number = self.n
    #     return number
    # numb()
variable = Var
print(variable)


# class Even:
#     def __init__(self, number):
#         super(Even, self).__init__(number)

# class Even(Var):
#     def __init__(self,number):
#         pass
#     def even(self, number):
#         if number  % 2 == 0:
#             return True
#         else:
#             return False


# Even_check = Even

# class Power(Even):