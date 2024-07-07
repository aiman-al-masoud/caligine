from lark import Lark, Transformer
from core.Asgn import Asgn
from core.Bool import Bool
from core.Def import Def
from core.FunCall import FunCall
from core.Id import Id
from core.Prog import Prog
from core.Var import Var
from core.Not import Not
from core.BinOp import BinOp
from core.Object import Object
from core.Dot import Dot
from core.Rule import Rule
from core.Num import Num
from core.Del import Del
from core.Print import Print
from core.Str import Str


class ToAst(Transformer):

    def IDENTIFIER(self, x):
        return str(x)

    def constant(self, xs):

        if xs[0]=='true':
            return Bool(True)
        elif xs[0]=='false':
            return Bool(False)
        else:
            return Id(xs[0])

    def VARIABLE(self, x):
        return Var(str(x))

    def NUMBER(self, x):
        return Num(float(x))

    def STRING(self, x):
        return Str(str(x))

    def exp_call(self, xs):
        return FunCall(xs[0], xs[1])

    def exp_not(self, xs):
        return Not(xs[1])

    def exp_add(self, xs):
        return BinOp('+', xs[0], xs[1])

    def exp_and(self, xs):
        return BinOp('and', xs[0], xs[1])

    def exp_or(self, xs):
        return BinOp('or', xs[0], xs[1])

    def exp_sub(self, xs):
        return BinOp('-', xs[0], xs[1])

    def exp_mul(self, xs):
        return BinOp('*', xs[0], xs[1])

    def exp_div(self, xs):
        return BinOp('/', xs[0], xs[1])

    def exp_gte(self, xs):
        return BinOp('>=', xs[0], xs[1])

    def exp_lte(self, xs):
        return BinOp('<=', xs[0], xs[1])

    def exp_gt(self, xs):
        return BinOp('>', xs[0], xs[1])

    def exp_lt(self, xs):
        return BinOp('<', xs[0], xs[1])

    def exp_eq(self, xs):
        return BinOp('==', xs[0], xs[1])

    def kwarg(self, xs):
        return {xs[0]:xs[1], **( xs[2] if len(xs)==3 else  {}) }

    def object(self, xs):
        return Object(xs[1], xs[0], xs[2])

    def arg(self, xs):

        if len(xs)==2:
            return [xs[0], *xs[1]]
        else:
            return xs

    def exp_rule(self, xs):
        return Rule(xs[0], xs[1])

    def exp_def(self, xs):

        fun_call = xs[0]
        assert isinstance(fun_call, FunCall)
        return Def(fun_call.fun_name, fun_call.args, xs[1])

    def statement(self, xs):
        return Prog(xs)

    def exp_dot(self, xs):
        return Dot(xs[0], xs[1])
    
    def exp_asgn(self, xs):

        dot = xs[0]
        assert isinstance(dot, Dot)
        return Asgn(dot.owner, dot.key, xs[1])

    def exp_del(self, xs):
        return Del(xs[0])

    def exp_print(self, xs):
        return Print(xs[1])
