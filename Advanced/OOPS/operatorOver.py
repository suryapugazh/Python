# Operator Overloading.
# Why for --> because we can't add or sub or else with Two Objects.
# This is called Magic Method.

class Add:
    def __init__(self,a):
        self.a = a

    def __add__(abcd, efgh):     # we can pass two argument for each object, we can put any name for that. Here abcd referred as "self".
        return abcd.a + efgh.a   # return addition of two object that stored in "a" from __init__ constructor. "abcd" as First Object on Stack, "efgh" as Second Object on Stack, and both accessing by "a" and Add.
    
    def __sub__(ijkl, mnop):
        return ijkl.a - mnop.a
        

o1 = Add(10)                     # object 1 created with 10 and store it to "Stack" on "a".
o2 = Add(20)                     # object 2 created with 20 and store it to "Stack" on "a.
print("Total : ", o1 + o2)       # here "+" operator is referred as __add__ constructor and return "abcd.a + efgh.a" objects.
print("Total : ", o1 - o2)

# Other similar Magic Method, source from Tutor Joes.
# https://www.tutorjoes.in/python_programming_tutorial/Operator_Overloading_in_python

"""
Operator	Magic Method
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
 
Comparison Operators :
Operator	Magic Method
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
 
Assignment Operators :
Operator	Magic Method
-=	__ISUB__(SELF, OTHER)
+=	__IADD__(SELF, OTHER)
*=	__IMUL__(SELF, OTHER)
/=	__IDIV__(SELF, OTHER)
//=	__IFLOORDIV__(SELF, OTHER)
%=	__IMOD__(SELF, OTHER)
**=	__IPOW__(SELF, OTHER)
>>=	__IRSHIFT__(SELF, OTHER)
<<=	__ILSHIFT__(SELF, OTHER)
&=	__IAND__(SELF, OTHER)
|=	__IOR__(SELF, OTHER)
^=	__IXOR__(SELF, OTHER)
 
Unary Operators :
Operator	Magic Method
-	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
 
"""