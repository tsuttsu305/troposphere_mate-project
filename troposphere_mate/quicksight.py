# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.quicksight

from troposphere.quicksight import (
    AdHocFilteringOption as _AdHocFilteringOption,
    AnalysisError as _AnalysisError,
    AnalysisSourceEntity as _AnalysisSourceEntity,
    AnalysisSourceTemplate as _AnalysisSourceTemplate,
    BorderStyle as _BorderStyle,
    DashboardPublishOptions as _DashboardPublishOptions,
    DashboardSourceEntity as _DashboardSourceEntity,
    DashboardSourceTemplate as _DashboardSourceTemplate,
    DataColorPalette as _DataColorPalette,
    DataSetReference as _DataSetReference,
    DateTimeParameter as _DateTimeParameter,
    DecimalParameter as _DecimalParameter,
    ExportToCSVOption as _ExportToCSVOption,
    Font as _Font,
    GutterStyle as _GutterStyle,
    IntegerParameter as _IntegerParameter,
    MarginStyle as _MarginStyle,
    Parameters as _Parameters,
    ResourcePermission as _ResourcePermission,
    SheetControlsOption as _SheetControlsOption,
    SheetStyle as _SheetStyle,
    StringParameter as _StringParameter,
    Tags as _Tags,
    TemplateSourceAnalysis as _TemplateSourceAnalysis,
    TemplateSourceEntity as _TemplateSourceEntity,
    TemplateSourceTemplate as _TemplateSourceTemplate,
    ThemeConfiguration as _ThemeConfiguration,
    TileLayoutStyle as _TileLayoutStyle,
    TileStyle as _TileStyle,
    Typography as _Typography,
    UIColorPalette as _UIColorPalette,
    double as _double,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class AnalysisError(troposphere.quicksight.AnalysisError, Mixin):
    def __init__(self,
                 title=None,
                 Message=NOTHING, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Message=Message,
            Type=Type,
            **kwargs
        )
        super(AnalysisError, self).__init__(**processed_kwargs)


class DataSetReference(troposphere.quicksight.DataSetReference, Mixin):
    def __init__(self,
                 title=None,
                 DataSetArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataSetPlaceholder=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataSetArn=DataSetArn,
            DataSetPlaceholder=DataSetPlaceholder,
            **kwargs
        )
        super(DataSetReference, self).__init__(**processed_kwargs)


class AnalysisSourceTemplate(troposphere.quicksight.AnalysisSourceTemplate, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataSetReferences=REQUIRED, # type: List[_DataSetReference]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            DataSetReferences=DataSetReferences,
            **kwargs
        )
        super(AnalysisSourceTemplate, self).__init__(**processed_kwargs)


class AnalysisSourceEntity(troposphere.quicksight.AnalysisSourceEntity, Mixin):
    def __init__(self,
                 title=None,
                 SourceTemplate=NOTHING, # type: _AnalysisSourceTemplate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourceTemplate=SourceTemplate,
            **kwargs
        )
        super(AnalysisSourceEntity, self).__init__(**processed_kwargs)


class DateTimeParameter(troposphere.quicksight.DateTimeParameter, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Values=Values,
            **kwargs
        )
        super(DateTimeParameter, self).__init__(**processed_kwargs)


class DecimalParameter(troposphere.quicksight.DecimalParameter, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=REQUIRED, # type: List[_double]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Values=Values,
            **kwargs
        )
        super(DecimalParameter, self).__init__(**processed_kwargs)


class IntegerParameter(troposphere.quicksight.IntegerParameter, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=REQUIRED, # type: List[_double]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Values=Values,
            **kwargs
        )
        super(IntegerParameter, self).__init__(**processed_kwargs)


class StringParameter(troposphere.quicksight.StringParameter, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Values=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Values=Values,
            **kwargs
        )
        super(StringParameter, self).__init__(**processed_kwargs)


class Parameters(troposphere.quicksight.Parameters, Mixin):
    def __init__(self,
                 title=None,
                 DateTimeParameters=NOTHING, # type: List[_DateTimeParameter]
                 DecimalParameters=NOTHING, # type: List[_DecimalParameter]
                 IntegerParameters=NOTHING, # type: List[_IntegerParameter]
                 StringParameters=NOTHING, # type: List[_StringParameter]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DateTimeParameters=DateTimeParameters,
            DecimalParameters=DecimalParameters,
            IntegerParameters=IntegerParameters,
            StringParameters=StringParameters,
            **kwargs
        )
        super(Parameters, self).__init__(**processed_kwargs)


class ResourcePermission(troposphere.quicksight.ResourcePermission, Mixin):
    def __init__(self,
                 title=None,
                 Actions=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Principal=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Actions=Actions,
            Principal=Principal,
            **kwargs
        )
        super(ResourcePermission, self).__init__(**processed_kwargs)


class Analysis(troposphere.quicksight.Analysis, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AnalysisId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AwsAccountId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Errors=NOTHING, # type: List[_AnalysisError]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: _Parameters
                 Permissions=NOTHING, # type: List[_ResourcePermission]
                 SourceEntity=NOTHING, # type: _AnalysisSourceEntity
                 Tags=NOTHING, # type: _Tags
                 ThemeArn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AnalysisId=AnalysisId,
            AwsAccountId=AwsAccountId,
            Errors=Errors,
            Name=Name,
            Parameters=Parameters,
            Permissions=Permissions,
            SourceEntity=SourceEntity,
            Tags=Tags,
            ThemeArn=ThemeArn,
            **kwargs
        )
        super(Analysis, self).__init__(**processed_kwargs)


class AdHocFilteringOption(troposphere.quicksight.AdHocFilteringOption, Mixin):
    def __init__(self,
                 title=None,
                 AvailabilityStatus=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AvailabilityStatus=AvailabilityStatus,
            **kwargs
        )
        super(AdHocFilteringOption, self).__init__(**processed_kwargs)


class ExportToCSVOption(troposphere.quicksight.ExportToCSVOption, Mixin):
    def __init__(self,
                 title=None,
                 AvailabilityStatus=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AvailabilityStatus=AvailabilityStatus,
            **kwargs
        )
        super(ExportToCSVOption, self).__init__(**processed_kwargs)


class SheetControlsOption(troposphere.quicksight.SheetControlsOption, Mixin):
    def __init__(self,
                 title=None,
                 VisibilityState=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            VisibilityState=VisibilityState,
            **kwargs
        )
        super(SheetControlsOption, self).__init__(**processed_kwargs)


class DashboardPublishOptions(troposphere.quicksight.DashboardPublishOptions, Mixin):
    def __init__(self,
                 title=None,
                 AdHocFilteringOption=NOTHING, # type: _AdHocFilteringOption
                 ExportToCSVOption=NOTHING, # type: _ExportToCSVOption
                 SheetControlsOption=NOTHING, # type: _SheetControlsOption
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AdHocFilteringOption=AdHocFilteringOption,
            ExportToCSVOption=ExportToCSVOption,
            SheetControlsOption=SheetControlsOption,
            **kwargs
        )
        super(DashboardPublishOptions, self).__init__(**processed_kwargs)


class DashboardSourceTemplate(troposphere.quicksight.DashboardSourceTemplate, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataSetReferences=REQUIRED, # type: List[_DataSetReference]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            DataSetReferences=DataSetReferences,
            **kwargs
        )
        super(DashboardSourceTemplate, self).__init__(**processed_kwargs)


class DashboardSourceEntity(troposphere.quicksight.DashboardSourceEntity, Mixin):
    def __init__(self,
                 title=None,
                 SourceTemplate=NOTHING, # type: _DashboardSourceTemplate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourceTemplate=SourceTemplate,
            **kwargs
        )
        super(DashboardSourceEntity, self).__init__(**processed_kwargs)


class Dashboard(troposphere.quicksight.Dashboard, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AwsAccountId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DashboardId=REQUIRED, # type: Union[str, AWSHelperFn]
                 DashboardPublishOptions=NOTHING, # type: _DashboardPublishOptions
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: _Parameters
                 Permissions=NOTHING, # type: List[_ResourcePermission]
                 SourceEntity=NOTHING, # type: _DashboardSourceEntity
                 Tags=NOTHING, # type: _Tags
                 ThemeArn=NOTHING, # type: Union[str, AWSHelperFn]
                 VersionDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AwsAccountId=AwsAccountId,
            DashboardId=DashboardId,
            DashboardPublishOptions=DashboardPublishOptions,
            Name=Name,
            Parameters=Parameters,
            Permissions=Permissions,
            SourceEntity=SourceEntity,
            Tags=Tags,
            ThemeArn=ThemeArn,
            VersionDescription=VersionDescription,
            **kwargs
        )
        super(Dashboard, self).__init__(**processed_kwargs)


class TemplateSourceAnalysis(troposphere.quicksight.TemplateSourceAnalysis, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataSetReferences=REQUIRED, # type: List[_DataSetReference]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            DataSetReferences=DataSetReferences,
            **kwargs
        )
        super(TemplateSourceAnalysis, self).__init__(**processed_kwargs)


class TemplateSourceTemplate(troposphere.quicksight.TemplateSourceTemplate, Mixin):
    def __init__(self,
                 title=None,
                 Arn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Arn=Arn,
            **kwargs
        )
        super(TemplateSourceTemplate, self).__init__(**processed_kwargs)


class TemplateSourceEntity(troposphere.quicksight.TemplateSourceEntity, Mixin):
    def __init__(self,
                 title=None,
                 SourceAnalysis=NOTHING, # type: _TemplateSourceAnalysis
                 SourceTemplate=NOTHING, # type: _TemplateSourceTemplate
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourceAnalysis=SourceAnalysis,
            SourceTemplate=SourceTemplate,
            **kwargs
        )
        super(TemplateSourceEntity, self).__init__(**processed_kwargs)


class Template(troposphere.quicksight.Template, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AwsAccountId=REQUIRED, # type: Union[str, AWSHelperFn]
                 TemplateId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Permissions=NOTHING, # type: List[_ResourcePermission]
                 SourceEntity=NOTHING, # type: _TemplateSourceEntity
                 Tags=NOTHING, # type: _Tags
                 VersionDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AwsAccountId=AwsAccountId,
            TemplateId=TemplateId,
            Name=Name,
            Permissions=Permissions,
            SourceEntity=SourceEntity,
            Tags=Tags,
            VersionDescription=VersionDescription,
            **kwargs
        )
        super(Template, self).__init__(**processed_kwargs)


class DataColorPalette(troposphere.quicksight.DataColorPalette, Mixin):
    def __init__(self,
                 title=None,
                 Colors=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 EmptyFillColor=NOTHING, # type: Union[str, AWSHelperFn]
                 MinMaxGradient=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Colors=Colors,
            EmptyFillColor=EmptyFillColor,
            MinMaxGradient=MinMaxGradient,
            **kwargs
        )
        super(DataColorPalette, self).__init__(**processed_kwargs)


class GutterStyle(troposphere.quicksight.GutterStyle, Mixin):
    def __init__(self,
                 title=None,
                 Show=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Show=Show,
            **kwargs
        )
        super(GutterStyle, self).__init__(**processed_kwargs)


class MarginStyle(troposphere.quicksight.MarginStyle, Mixin):
    def __init__(self,
                 title=None,
                 Show=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Show=Show,
            **kwargs
        )
        super(MarginStyle, self).__init__(**processed_kwargs)


class TileLayoutStyle(troposphere.quicksight.TileLayoutStyle, Mixin):
    def __init__(self,
                 title=None,
                 Gutter=NOTHING, # type: _GutterStyle
                 Margin=NOTHING, # type: _MarginStyle
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Gutter=Gutter,
            Margin=Margin,
            **kwargs
        )
        super(TileLayoutStyle, self).__init__(**processed_kwargs)


class BorderStyle(troposphere.quicksight.BorderStyle, Mixin):
    def __init__(self,
                 title=None,
                 Show=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Show=Show,
            **kwargs
        )
        super(BorderStyle, self).__init__(**processed_kwargs)


class TileStyle(troposphere.quicksight.TileStyle, Mixin):
    def __init__(self,
                 title=None,
                 Border=NOTHING, # type: _BorderStyle
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Border=Border,
            **kwargs
        )
        super(TileStyle, self).__init__(**processed_kwargs)


class SheetStyle(troposphere.quicksight.SheetStyle, Mixin):
    def __init__(self,
                 title=None,
                 Tile=NOTHING, # type: _TileStyle
                 TileLayout=NOTHING, # type: _TileLayoutStyle
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Tile=Tile,
            TileLayout=TileLayout,
            **kwargs
        )
        super(SheetStyle, self).__init__(**processed_kwargs)


class Font(troposphere.quicksight.Font, Mixin):
    def __init__(self,
                 title=None,
                 FontFamily=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FontFamily=FontFamily,
            **kwargs
        )
        super(Font, self).__init__(**processed_kwargs)


class Typography(troposphere.quicksight.Typography, Mixin):
    def __init__(self,
                 title=None,
                 FontFamilies=NOTHING, # type: List[_Font]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FontFamilies=FontFamilies,
            **kwargs
        )
        super(Typography, self).__init__(**processed_kwargs)


class UIColorPalette(troposphere.quicksight.UIColorPalette, Mixin):
    def __init__(self,
                 title=None,
                 Accent=NOTHING, # type: Union[str, AWSHelperFn]
                 AccentForeground=NOTHING, # type: Union[str, AWSHelperFn]
                 Danger=NOTHING, # type: Union[str, AWSHelperFn]
                 DangerForeground=NOTHING, # type: Union[str, AWSHelperFn]
                 Dimension=NOTHING, # type: Union[str, AWSHelperFn]
                 DimensionForeground=NOTHING, # type: Union[str, AWSHelperFn]
                 Measure=NOTHING, # type: Union[str, AWSHelperFn]
                 MeasureForeground=NOTHING, # type: Union[str, AWSHelperFn]
                 PrimaryBackground=NOTHING, # type: Union[str, AWSHelperFn]
                 PrimaryForeground=NOTHING, # type: Union[str, AWSHelperFn]
                 SecondaryBackground=NOTHING, # type: Union[str, AWSHelperFn]
                 SecondaryForeground=NOTHING, # type: Union[str, AWSHelperFn]
                 Success=NOTHING, # type: Union[str, AWSHelperFn]
                 SuccessForeground=NOTHING, # type: Union[str, AWSHelperFn]
                 Warning=NOTHING, # type: Union[str, AWSHelperFn]
                 WarningForeground=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Accent=Accent,
            AccentForeground=AccentForeground,
            Danger=Danger,
            DangerForeground=DangerForeground,
            Dimension=Dimension,
            DimensionForeground=DimensionForeground,
            Measure=Measure,
            MeasureForeground=MeasureForeground,
            PrimaryBackground=PrimaryBackground,
            PrimaryForeground=PrimaryForeground,
            SecondaryBackground=SecondaryBackground,
            SecondaryForeground=SecondaryForeground,
            Success=Success,
            SuccessForeground=SuccessForeground,
            Warning=Warning,
            WarningForeground=WarningForeground,
            **kwargs
        )
        super(UIColorPalette, self).__init__(**processed_kwargs)


class ThemeConfiguration(troposphere.quicksight.ThemeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DataColorPalette=NOTHING, # type: _DataColorPalette
                 Sheet=NOTHING, # type: _SheetStyle
                 Typography=NOTHING, # type: _Typography
                 UIColorPalette=NOTHING, # type: _UIColorPalette
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataColorPalette=DataColorPalette,
            Sheet=Sheet,
            Typography=Typography,
            UIColorPalette=UIColorPalette,
            **kwargs
        )
        super(ThemeConfiguration, self).__init__(**processed_kwargs)


class Theme(troposphere.quicksight.Theme, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AwsAccountId=REQUIRED, # type: Union[str, AWSHelperFn]
                 ThemeId=REQUIRED, # type: Union[str, AWSHelperFn]
                 BaseThemeId=NOTHING, # type: Union[str, AWSHelperFn]
                 Configuration=NOTHING, # type: _ThemeConfiguration
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Permissions=NOTHING, # type: List[_ResourcePermission]
                 Tags=NOTHING, # type: _Tags
                 VersionDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AwsAccountId=AwsAccountId,
            ThemeId=ThemeId,
            BaseThemeId=BaseThemeId,
            Configuration=Configuration,
            Name=Name,
            Permissions=Permissions,
            Tags=Tags,
            VersionDescription=VersionDescription,
            **kwargs
        )
        super(Theme, self).__init__(**processed_kwargs)
