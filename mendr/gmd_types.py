#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x70f6b47b

# Compiled with Coconut version 3.1.2

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.2', '', False)
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and str('__coconut_cache__') in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != str('__coconut_cache__'):
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

from beartype.vale import Is  #1 (line in Coconut source)
try:  #2 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #2 (line in Coconut source)
except _coconut.NameError:  #2 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #2 (line in Coconut source)
sys = _coconut_sys  #2 (line in Coconut source)
if sys.version_info >= (3, 9):  #2 (line in Coconut source)
    if _coconut.typing.TYPE_CHECKING:  #2 (line in Coconut source)
        from typing import Annotated  #2 (line in Coconut source)
    else:  #2 (line in Coconut source)
        try:  #2 (line in Coconut source)
            Annotated = _coconut.typing.Annotated  #2 (line in Coconut source)
        except _coconut.AttributeError as _coconut_imp_err:  #2 (line in Coconut source)
            raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #2 (line in Coconut source)
else:  #2 (line in Coconut source)
    from typing_extensions import Annotated  #2 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #2 (line in Coconut source)
    sys = _coconut_sys_0  #2 (line in Coconut source)
import networkx as nx  #3 (line in Coconut source)

def _coconut_lambda_0(n  # type: int  #5 (line in Coconut source)
    ):  #5 (line in Coconut source)
    return n > 0  #5 (line in Coconut source)

PosInt = Annotated[int, Is[_coconut_lambda_0]]  # type: _coconut.typing.TypeAlias  #5 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #5 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #5 (line in Coconut source)
__annotations__["PosInt"] = _coconut.typing.TypeAlias  #5 (line in Coconut source)
ReturnsGraph = _coconut.typing.Callable[[PosInt, ...], nx.Graph]  # type: _coconut.typing.TypeAlias  # could refactor to (ReturnsNX | Returns ...)  #6 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # could refactor to (ReturnsNX | Returns ...)  #6 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # could refactor to (ReturnsNX | Returns ...)  #6 (line in Coconut source)
__annotations__["ReturnsGraph"] = _coconut.typing.TypeAlias  # could refactor to (ReturnsNX | Returns ...)  #6 (line in Coconut source)
