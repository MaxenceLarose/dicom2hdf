"""
    @file:              patient_data_query_strategy.py
    @Author:            Maxence Larose

    @Creation Date:     10/2021
    @Last modification: 03/2022

    @Description:       This file contains the class PatientDataQueryStrategies that enumerates the available categories
                        for the queries a user can make to obtain a patient's data.
"""

from enum import Enum
from typing import NamedTuple, Callable

from .factories.patient_data_factories import DefaultPatientDataFactory, SegmentationPatientDataFactory, \
    SeriesDescriptionPatientDataFactory, SegAndSeriesPatientDataFactory


class PatientDataQueryStrategy(NamedTuple):
    name: str
    factory: Callable


class PatientDataQueryStrategies(Enum):

    DEFAULT = PatientDataQueryStrategy(
        name="Default",
        factory=DefaultPatientDataFactory
    )

    SEGMENTATION = PatientDataQueryStrategy(
        name="Segmentation",
        factory=SegmentationPatientDataFactory
    )

    SERIES_DESCRIPTION = PatientDataQueryStrategy(
        name="Series description",
        factory=SeriesDescriptionPatientDataFactory
    )

    SEGMENTATION_AND_SERIES_DESCRIPTION = PatientDataQueryStrategy(
        name="Segmentation and series description",
        factory=SegAndSeriesPatientDataFactory
    )
