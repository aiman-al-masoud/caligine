import os
from lark import Lark, Transformer, v_args
from core.Asgn import Asgn
from core.Bool import Bool
from core.Def import Def
from core.Find import Find
from core.FunCall import FunCall
from core.Id import Id
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

        path_grammar = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'grammar.lark')

        self.lark = Lark(
            grammar=open(path_grammar).read(), 
            ambiguity='explicit', 
            lexer='basic',
            propagate_positions=True,
        )
        self.toast = ToAst()
    
    def parse(self, text:str)->Ast:

        st = self.lark.parse(text)
        ast = self.toast.transform(st)
        return ast

class ToAst(Transformer):

    def CNAME(self, x):

        x = str(x)

        if x == 'true':
            return Bool(True)
        elif x == 'false':
            return Bool(False)
        elif x.isupper():
            return Var(x)
        else:
            return Id(x)

    def NUMBER(self, x):
        return Num(float(x))

    def STRING(self, x):
        
        x = str(x).strip('"')
        return Str(x)

    @v_args(meta=True)
    def exp_call(self, meta, xs):

        x0 = xs[0]
        assert isinstance(x0, Id)
        return FunCall(x0.name, xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_not(self, meta, xs):
        return Not(xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_add(self, meta, xs):
        return BinOp('+', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_and(self, meta, xs):
        return BinOp('and', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_or(self, meta, xs):
        return BinOp('or', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_sub(self, meta, xs):
        return BinOp('-', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_mul(self, meta, xs):
        return BinOp('*', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_div(self, meta, xs):
        return BinOp('/', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_gte(self, meta, xs):
        return BinOp('>=', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_lte(self, meta, xs):
        return BinOp('<=', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_gt(self, meta, xs):
        return BinOp('>', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_lt(self, meta, xs):
        return BinOp('<', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_eq(self, meta, xs):
        return BinOp('==', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_neq(self, meta, xs):
        return BinOp('!=', xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def object(self, meta, xs):

        x0 = xs[0]
        x1 = xs[1]
        assert isinstance(x0, Id)
        assert isinstance(x1, Id)
        props = xs[2] if len(xs) > 2 else {}

        match x0.name:
            case 'sprite': return Sprite(x1.name, props).set_meta_info(MetaInfo.from_lark(meta))
            case 'client': return Client(x1.name, props).set_meta_info(MetaInfo.from_lark(meta))
            case 'keyboard': return Object(x1.name, props).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def sequence(self, meta, xs):
        return Sequence(xs[0]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_rule(self, meta, xs):
        return Rule(xs[0], xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_def(self, meta, xs):

        fun_call = xs[0]
        assert isinstance(fun_call, FunCall)
        return Def(fun_call.fun_name, fun_call.args, xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_prog(self, meta, xs):
        return Prog(xs).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_dot(self, meta, xs):
        
        x1 = xs[1]
        assert isinstance(x1, Id)
        return Dot(xs[0], x1.name).set_meta_info(MetaInfo.from_lark(meta))
    
    @v_args(meta=True)
    def exp_asgn(self, meta, xs):

        dot = xs[0]
        assert isinstance(dot, Dot)
        return Asgn(dot.owner, dot.key, xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_del(self, meta, xs):
        return Del(xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_print(self, meta, xs):
        return Print(xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_find(self, meta, xs):
        return Find(xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_create(self, meta, xs):
        return Create(xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    @v_args(meta=True)
    def exp_assert(self, meta, xs):
        return Assert(xs[1]).set_meta_info(MetaInfo.from_lark(meta))

    def pair(self, xs):

        x0 = xs[0]
        assert isinstance(x0, Id)
        return [Str(x0.name), xs[1]]

    def arg(self, xs):

        if len(xs)==2:
            return [xs[0], *xs[1]]
        else:
            return xs

    def kwarg(self, pairs):
        return { p[0] :p[1] for p in pairs}
