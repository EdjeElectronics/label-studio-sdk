# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class InferenceRunCostEstimate(pydantic_v1.BaseModel):
    prompt_cost_usd: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Cost of the prompt (in USD)
    """

    completion_cost_usd: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Cost of the completion (in USD)
    """

    total_cost_usd: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Total cost of the inference (in USD)
    """

    is_error: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Whether an error occurred or not
    """

    error_type: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Type of error (e.g. "Timeout", "Rate Limit", etc)
    """

    error_message: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Error message details
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}