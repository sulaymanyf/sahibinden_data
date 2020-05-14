# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = ev_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast
from datetime import datetime
import time.parser


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return time.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Attributes:
    a22: Optional[int] = None
    a24: Optional[int] = None
    a812: Optional[int] = None
    a810: Optional[int] = None
    a107889: Optional[int] = None
    a811: Optional[int] = None
    a23: Optional[str] = None
    a27: Optional[str] = None
    a103651: Optional[str] = None
    a106960: Optional[str] = None
    a98426: Optional[str] = None
    a20: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Attributes':
        assert isinstance(obj, dict)
        a22 = from_union([from_none, lambda x: int(from_str(x))], obj.get("a22"))
        a24 = from_union([from_none, lambda x: int(from_str(x))], obj.get("a24"))
        a812 = from_union([from_none, lambda x: int(from_str(x))], obj.get("a812"))
        a810 = from_union([from_none, lambda x: int(from_str(x))], obj.get("a810"))
        a107889 = from_union([from_none, lambda x: int(from_str(x))], obj.get("a107889"))
        a811 = from_union([from_none, lambda x: int(from_str(x))], obj.get("a811"))
        a23 = from_union([from_str, from_none], obj.get("a23"))
        a27 = from_union([from_str, from_none], obj.get("a27"))
        a103651 = from_union([from_str, from_none], obj.get("a103651"))
        a106960 = from_union([from_str, from_none], obj.get("a106960"))
        a98426 = from_union([from_str, from_none], obj.get("a98426"))
        a20 = from_union([from_str, from_none], obj.get("a20"))
        return Attributes(a22, a24, a812, a810, a107889, a811, a23, a27, a103651, a106960, a98426, a20)

    def to_dict(self) -> dict:
        result: dict = {}
        result["a22"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.a22)
        result["a24"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.a24)
        result["a812"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.a812)
        result["a810"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.a810)
        result["a107889"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.a107889)
        result["a811"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.a811)
        result["a23"] = from_union([from_str, from_none], self.a23)
        result["a27"] = from_union([from_str, from_none], self.a27)
        result["a103651"] = from_union([from_str, from_none], self.a103651)
        result["a106960"] = from_union([from_str, from_none], self.a106960)
        result["a98426"] = from_union([from_str, from_none], self.a98426)
        result["a20"] = from_union([from_str, from_none], self.a20)
        return result


@dataclass
class TagAttributes:
    emlak_tipi: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TagAttributes':
        assert isinstance(obj, dict)
        emlak_tipi = from_union([from_str, from_none], obj.get("Emlak Tipi"))
        return TagAttributes(emlak_tipi)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Emlak Tipi"] = from_union([from_str, from_none], self.emlak_tipi)
        return result


@dataclass
class Ev:
    id: Optional[int] = None
    category_id: Optional[int] = None
    shortname: Optional[str] = None
    title: Optional[str] = None
    price: Optional[int] = None
    currency: Optional[str] = None
    formatted_price: Optional[str] = None
    classified_date: Optional[datetime] = None
    expiry_date: Optional[datetime] = None
    image_url: Optional[str] = None
    image_url_large_thumbnail: Optional[str] = None
    image_main_url: Optional[str] = None
    attributes: Optional[Attributes] = None
    tag_attributes: Optional[TagAttributes] = None
    location: Optional[str] = None
    active_promotions: Optional[List[int]] = None
    detailed_list_view_attributes: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Ev':
        assert isinstance(obj, dict)
        id = from_union([from_none, lambda x: int(from_str(x))], obj.get("id"))
        category_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("categoryId"))
        shortname = from_union([from_str, from_none], obj.get("shortname"))
        title = from_union([from_str, from_none], obj.get("title"))
        price = from_union([from_int, from_none], obj.get("price"))
        currency = from_union([from_str, from_none], obj.get("currency"))
        formatted_price = from_union([from_str, from_none], obj.get("formattedPrice"))
        classified_date = from_union([from_datetime, from_none], obj.get("classifiedDate"))
        expiry_date = from_union([from_datetime, from_none], obj.get("expiryDate"))
        image_url = from_union([from_str, from_none], obj.get("imageUrl"))
        image_url_large_thumbnail = from_union([from_str, from_none], obj.get("imageUrlLargeThumbnail"))
        image_main_url = from_union([from_str, from_none], obj.get("imageMainUrl"))
        attributes = from_union([Attributes.from_dict, from_none], obj.get("attributes"))
        tag_attributes = from_union([TagAttributes.from_dict, from_none], obj.get("tagAttributes"))
        location = from_union([from_str, from_none], obj.get("location"))
        active_promotions = from_union([lambda x: from_list(from_int, x), from_none], obj.get("activePromotions"))
        detailed_list_view_attributes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("detailedListViewAttributes"))
        return Ev(id, category_id, shortname, title, price, currency, formatted_price, classified_date, expiry_date, image_url, image_url_large_thumbnail, image_main_url, attributes, tag_attributes, location, active_promotions, detailed_list_view_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.id)
        result["categoryId"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.category_id)
        result["shortname"] = from_union([from_str, from_none], self.shortname)
        result["title"] = from_union([from_str, from_none], self.title)
        result["price"] = from_union([from_int, from_none], self.price)
        result["currency"] = from_union([from_str, from_none], self.currency)
        result["formattedPrice"] = from_union([from_str, from_none], self.formatted_price)
        result["classifiedDate"] = from_union([lambda x: x.isoformat(), from_none], self.classified_date)
        result["expiryDate"] = from_union([lambda x: x.isoformat(), from_none], self.expiry_date)
        result["imageUrl"] = from_union([from_str, from_none], self.image_url)
        result["imageUrlLargeThumbnail"] = from_union([from_str, from_none], self.image_url_large_thumbnail)
        result["imageMainUrl"] = from_union([from_str, from_none], self.image_main_url)
        result["attributes"] = from_union([lambda x: to_class(Attributes, x), from_none], self.attributes)
        result["tagAttributes"] = from_union([lambda x: to_class(TagAttributes, x), from_none], self.tag_attributes)
        result["location"] = from_union([from_str, from_none], self.location)
        result["activePromotions"] = from_union([lambda x: from_list(from_int, x), from_none], self.active_promotions)
        result["detailedListViewAttributes"] = from_union([lambda x: from_list(from_str, x), from_none], self.detailed_list_view_attributes)
        return result


def ev_from_dict(s: Any) -> Ev:
    return Ev.from_dict(s)


def ev_to_dict(x: Ev) -> Any:
    return to_class(Ev, x)
