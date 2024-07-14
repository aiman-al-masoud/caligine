import os
from lark import Lark, Transformer, v_args
from core.Asgn import Asgn
from core.Bool import Bool
from core.Def import Def
from core.Find import Find
from core.FunCall import FunCall
from core.Id import Id
from core.Keyboard import Keyboard
from core.MetaInfo import MetaInfo
from core.Prog import Prog
from core.Var import Var
from core.Not import Not
from core.BinOp import BinOp
from core.Object import Object
from core.Sprite import Sprite
from core.Client import Client
from core.Dot import Dot
from core.Rule import Rule
from core.Num import Num
from core.Del import Del
from core.Print import Print
from core.Str import Str
from core.Ast import Ast
from core.Assert import Assert
from core.Sequence import Sequence
from core.Create import Create


class Parser:

    def __init__(self):

        dir_current = os.path.split(os.path.abspath(__file__))[0]
        path_grammar = os.path.join(dir_current, 'grammar.lark')

        self.lark = Lark(
            grammar=open(path_grammar).read(),
            ambiguity='explicit',
            lexer='basic',
            propagate_positions=True,
        )

        self.toast = ToAst()

    def parse(self, text: str) -> Ast:

        st = self.lark.parse(text)
        ast = self.toast.transform(st)
        return ast


class ToAst(Transformer):

    @v_args(meta=True)
    def cname(self, meta, xs):

        x = xs[0]
        x = str(x)

        if x == 'true':
            return Bool(value=True, meta_info=MetaInfo(meta=meta))
        elif x == 'false':
            return Bool(value=False, meta_info=MetaInfo(meta=meta))
        elif x.isupper():
            return Var(name=x, meta_info=MetaInfo(meta=meta))
        else:
            return Id(name=x, meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def number(self, meta, xs):

        x = xs[0]
        return Num(value=float(x), meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def string(self, meta, xs):

        x = xs[0]
        x = str(x).strip('"')
        return Str(value=x, meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_call(self, meta, xs):

        x0 = xs[0]
        assert isinstance(x0, Id)
        return FunCall(fun_name=x0.name, args=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_not(self, meta, xs):
        return Not(negated=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_add(self, meta, xs):
        return BinOp(op='+', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_and(self, meta, xs):
        return BinOp(op='and', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_or(self, meta, xs):
        return BinOp(op='or', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_sub(self, meta, xs):
        return BinOp(op='-', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_mul(self, meta, xs):
        return BinOp(op='*', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_div(self, meta, xs):
        return BinOp(op='/', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_gte(self, meta, xs):
        return BinOp(op='>=', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_lte(self, meta, xs):
        return BinOp(op='<=', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_gt(self, meta, xs):
        return BinOp(op='>', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_lt(self, meta, xs):
        return BinOp(op='<', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_eq(self, meta, xs):
        return BinOp(op='==', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_neq(self, meta, xs):
        return BinOp(op='!=', left=xs[0], right=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def object(self, meta, xs):

        x0 = xs[0]
        x1 = xs[1]
        assert isinstance(x0, Id)
        assert isinstance(x1, Id)
        props = xs[2] if len(xs) > 2 else {}

        match x0.name:
            case 'sprite': return Sprite(name=x1.name, props=props, meta_info=MetaInfo(meta=meta))
            case 'client': return Client(name=x1.name, props=props, meta_info=MetaInfo(meta=meta))
            case 'keyboard': return Keyboard(name=x1.name, props=props, meta_info=MetaInfo(meta=meta))

        raise Exception()

    @v_args(meta=True)
    def sequence(self, meta, xs):
        return Sequence(values=xs[0], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_rule(self, meta, xs):
        return Rule(condition=xs[0], consequence=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_def(self, meta, xs):

        fun_call = xs[0]
        assert isinstance(fun_call, FunCall)
        return Def(name=fun_call.fun_name, args=fun_call.args, body=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_prog(self, meta, xs):
        return Prog(statements=xs, meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_dot(self, meta, xs):

        x1 = xs[1]
        assert isinstance(x1, Id)
        return Dot(owner=xs[0], key=x1.name, meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_asgn(self, meta, xs):

        dot = xs[0]
        assert isinstance(dot, Dot)
        return Asgn(owner=dot.owner, key=dot.key, value=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_del(self, meta, xs):
        return Del(delendum=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_print(self, meta, xs):
        return Print(prindandum=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_find(self, meta, xs):
        return Find(formula=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_create(self, meta, xs):
        return Create(creandum=xs[1], meta_info=MetaInfo(meta=meta))

    @v_args(meta=True)
    def exp_assert(self, meta, xs):
        return Assert(assertion=xs[1], meta_info=MetaInfo(meta=meta))

    def pair(self, xs):

        x0 = xs[0]
        assert isinstance(x0, Id)
        return [Str(value=x0.name), xs[1]]

    def arg(self, xs):

        if len(xs) == 2:
            return [xs[0], *xs[1]]
        else:
            return xs

    def kwarg(self, pairs):

        pairs = [p for p in pairs if p is not None]
        return {p[0]: p[1] for p in pairs}
