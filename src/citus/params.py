from enum import Enum
import typing as ty
from typing import Any, Callable, Dict, Optional, Sequence

from citus.pydantic.fields import FieldInfo, Undefined


class ParamTypes(Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"


class Param(FieldInfo):
    in_: ParamTypes

    def __init__(
        self,
        default: ty.Any,
        *,
        alias: ty.Optional[str] = None,
        title: ty.Optional[str] = None,
        description: ty.Optional[str] = None,
        gt: ty.Optional[float] = None,
        ge: ty.Optional[float] = None,
        lt: ty.Optional[float] = None,
        le: ty.Optional[float] = None,
        min_length: ty.Optional[int] = None,
        max_length: ty.Optional[int] = None,
        regex: ty.Optional[str] = None,
        example: ty.Any = Undefined,
        examples: ty.Optional[ty.Dict[str, ty.Any]] = None,
        deprecated: ty.Optional[bool] = None,
        **extra: ty.Any,
    ):
        self.deprecated = deprecated
        self.example = example
        self.examples = examples
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            **extra,
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.default})"


class Path(Param):
    """
    Used to declare more validations and metadata for path parameters
    :param default:
    :param alias:
    :param title:  The ID of the item to fetch
    :param description: A short description of the path Parameter
    """

    in_ = ParamTypes.path

    def __init__(
        self,
        default: Any,
        *,
        alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex: Optional[str] = None,
        example: Any = Undefined,
        examples: Optional[Dict[str, Any]] = None,
        deprecated: Optional[bool] = None,
        **extra: Any,
    ):
        self.in_ = self.in_
        super().__init__(
            ...,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            deprecated=deprecated,
            example=example,
            examples=examples,
            **extra,
        )


def path( # noqa: N802
        self,
        default: ty.Any,
        *,
        alias: ty.Optional[str] = None,
        title: ty.Optional[str] = None,
        description: ty.Optional[str] = None,
        gt: ty.Optional[float] = None,
        ge: ty.Optional[float] = None,
        lt: ty.Optional[float] = None,
        le: ty.Optional[float] = None,
        min_length: ty.Optional[int] = None,
        max_length: ty.Optional[int] = None,
        regex: ty.Optional[str] = None,
        example: ty.Any = Undefined,
        examples: ty.Optional[ty.Dict[str, ty.Any]] = None,
        deprecated: ty.Optional[bool] = None,
        **extra: ty.Any,
        ) -> ty.Any:
    return Path(
            default=default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            example=example,
            examples=examples,
            deprecated=deprecated,
            **extra,
            )

class Query(Param):
    in_ = ParamTypes.query

    def __init__(
        self,
        default: Any,
        *,
        alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex: Optional[str] = None,
        example: Any = Undefined,
        examples: Optional[Dict[str, Any]] = None,
        deprecated: Optional[bool] = None,
        **extra: Any,
    ):
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            deprecated=deprecated,
            example=example,
            examples=examples,
            **extra,
        )


def query(  # noqa: N802
        default: Any,
        *,
        alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex: Optional[str] = None,
        example: Any = Undefined,
        examples: Optional[Dict[str, Any]] = None,
        deprecated: Optional[bool] = None,
        **extra: Any,
        ) -> Any:

    return Query(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            example=example,
            examples=examples,
            deprecated=deprecated,
            **extra,
            )


class Header(Param):
    in_ = ParamTypes.header

    def __init__(
        self,
        default: Any,
        *,
        alias: Optional[str] = None,
        convert_underscores: bool = True,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex: Optional[str] = None,
        example: Any = Undefined,
        examples: Optional[Dict[str, Any]] = None,
        deprecated: Optional[bool] = None,
        **extra: Any,
    ):
        self.convert_underscores = convert_underscores
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            deprecated=deprecated,
            example=example,
            examples=examples,
            **extra,
        )

def header(  # noqa: N802
    default: ty.Any,
    *,
    alias: ty.Optional[str] = None,
    convert_underscores: bool = True,
    title: ty.Optional[str] = None,
    description: ty.Optional[str] = None,
    gt: ty.Optional[float] = None,
    ge: ty.Optional[float] = None,
    lt: ty.Optional[float] = None,
    le: ty.Optional[float] = None,
    min_length: ty.Optional[int] = None,
    max_length: ty.Optional[int] = None,
    regex: ty.Optional[str] = None,
    example: ty.Any = Undefined,
    examples: ty.Optional[ty.Dict[str, ty.Any]] = None,
    deprecated: ty.Optional[bool] = None,
    **extra: ty.Any,
) -> ty.Any:

    return Header(
        default,
        alias=alias,
        convert_underscores=convert_underscores,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        deprecated=deprecated,
        **extra,
    )


class Cookie(Param):
    in_ = ParamTypes.cookie

    def __init__(
        self,
        default: Any,
        *,
        alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex: Optional[str] = None,
        example: Any = Undefined,
        examples: Optional[Dict[str, Any]] = None,
        deprecated: Optional[bool] = None,
        **extra: Any,
    ):
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            deprecated=deprecated,
            example=example,
            examples=examples,
            **extra,
        )


def cookie(  # noqa: N802
    default: ty.Any,
    *,
    alias: ty.Optional[str] = None,
    title: ty.Optional[str] = None,
    description: ty.Optional[str] = None,
    gt: ty.Optional[float] = None,
    ge: ty.Optional[float] = None,
    lt: ty.Optional[float] = None,
    le: ty.Optional[float] = None,
    min_length: ty.Optional[int] = None,
    max_length: ty.Optional[int] = None,
    regex: ty.Optional[str] = None,
    example: ty.Any = Undefined,
    examples: ty.Optional[ty.Dict[str, ty.Any]] = None,
    deprecated: ty.Optional[bool] = None,
    **extra: ty.Any,
) -> ty.Any:
    return Cookie(
        default,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        deprecated=deprecated,
        **extra,
    )



class Body(FieldInfo):
    def __init__(
        self,
        default: Any,
        *,
        embed: bool = False,
        media_type: str = "application/json",
        alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex: Optional[str] = None,
        example: Any = Undefined,
        examples: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ):
        self.embed = embed
        self.media_type = media_type
        self.example = example
        self.examples = examples
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            **extra,
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.default})"


def body(  # noqa: N802
    default: Any,
    *,
    embed: bool = False,
    media_type: str = "application/json",
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    **extra: Any,
) -> Any:
    return Body(
        default,
        embed=embed,
        media_type=media_type,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        **extra,
    )

class Form(Body):
    def __init__(
        self,
        default: Any,
        *,
        media_type: str = "application/x-www-form-urlencoded",
        alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex: Optional[str] = None,
        example: Any = Undefined,
        examples: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ):
        super().__init__(
            default,
            embed=True,
            media_type=media_type,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            example=example,
            examples=examples,
            **extra,
        )

def form(  # noqa: N802
    default: Any,
    *,
    media_type: str = "application/x-www-form-urlencoded",
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    **extra: Any,
) -> Any:
    return Form(
        default,
        media_type=media_type,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        **extra,
    )


class File(Form):
    def __init__(
        self,
        default: ty.Any,
        *,
        media_type: str = "multiparse/form-data",
        alias: ty.Optional[str] = None,
        title: ty.Optional[str] = None,
        description: ty.Optional[str] = None,
        gt: ty.Optional[float] = None,
        ge: ty.Optional[float] = None,
        lt: ty.Optional[float] = None,
        le: ty.Optional[float] = None,
        min_length: ty.Optional[int] = None,
        max_length: ty.Optional[int] = None,
        regex: ty.Optional[str] = None,
        example: ty.Any = Undefined,
        examples: ty.Optional[ty.Dict[str, ty.Any]] = None,
        **extra: ty.Any,
    ):
        super().__init__(
            default,
            media_type=media_type,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            example=example,
            examples=examples,
            **extra,
        )

def file(  # noqa: N802
    default: ty.Any,
    *,
    media_type: str = "multiparse/form-data",
    alias: ty.Optional[str] = None,
    title: ty.Optional[str] = None,
    description: Optional[str] = None,
    gt: ty.Optional[float] = None,
    ge: ty.Optional[float] = None,
    lt: ty.Optional[float] = None,
    le: ty.Optional[float] = None,
    min_length: ty.Optional[int] = None,
    max_length: ty.Optional[int] = None,
    regex: ty.Optional[str] = None,
    example: ty.Any = Undefined,
    examples: ty.Optional[ty.Dict[str, ty.Any]] = None,
    **extra: ty.Any,
) -> ty.Any:
    return File(
        default,
        media_type=media_type,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        **extra,
    )


class Depends:
    def __init__(
            self, 
            dependency: ty.Optional[ty.Callable[..., ty.Any]] = None,
            *, 
            use_cache: bool = True
            ):
        self.dependency = dependency
        self.use_cache = use_cache

    def __repr__(self) -> str:
        attr = getattr(self.dependency, "__name__", type(self.dependency).__name__)
        cache = "" if self.use_cache else ", use_cache=False"
        return f"{self.__class__.__name__}({attr}{cache})"



def depends(  # noqa: N802
        dependency: ty.Optional[ty.Callable[..., ty.Any]] = None,
        *, use_cache: bool = True
        ) -> ty.Any:
    return Depends(
            dependency=dependency, 
            use_cache=use_cache
            )


class Security(Depends):
    def __init__(
            self,
            dependency: ty.Optional[ty.Callable[..., ty.Any]] = None,
            *,
            scopes: ty.Optional[ty.Sequence[str]] = None,
            use_cache: bool = True,
            ):

        super().__init__(
                dependency=dependency, 
                use_cache=use_cache
                )
        self.scopes = scopes or []



def security(  # noqa: N802
    dependency: ty.Optional[ty.Callable[..., ty.Any]] = None,
    *,
    scopes: ty.Optional[ty.Sequence[str]] = None,
    use_cache: bool = True,
    ) -> ty.Any:
    return Security(
            dependency=dependency, 
            scopes=scopes,
            use_cache=use_cache
            )
