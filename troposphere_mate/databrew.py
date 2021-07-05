# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.databrew

from troposphere.databrew import (
    Action as _Action,
    ConditionExpression as _ConditionExpression,
    CsvOutputOptions as _CsvOutputOptions,
    DataCatalogInputDefinition as _DataCatalogInputDefinition,
    Output as _Output,
    OutputFormatOptions as _OutputFormatOptions,
    RecipeParameters as _RecipeParameters,
    RecipeStep as _RecipeStep,
    S3Location as _S3Location,
    SecondaryInput as _SecondaryInput,
    Tags as _Tags,
    integer as _integer,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class Dataset(troposphere.databrew.Dataset, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Input=REQUIRED, # type: dict
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Format=NOTHING, # type: Union[str, AWSHelperFn]
                 FormatOptions=NOTHING, # type: dict
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Input=Input,
            Name=Name,
            Format=Format,
            FormatOptions=FormatOptions,
            Tags=Tags,
            **kwargs
        )
        super(Dataset, self).__init__(**processed_kwargs)


class CsvOutputOptions(troposphere.databrew.CsvOutputOptions, Mixin):
    def __init__(self,
                 title=None,
                 Delimiter=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Delimiter=Delimiter,
            **kwargs
        )
        super(CsvOutputOptions, self).__init__(**processed_kwargs)


class OutputFormatOptions(troposphere.databrew.OutputFormatOptions, Mixin):
    def __init__(self,
                 title=None,
                 Csv=NOTHING, # type: _CsvOutputOptions
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Csv=Csv,
            **kwargs
        )
        super(OutputFormatOptions, self).__init__(**processed_kwargs)


class S3Location(troposphere.databrew.S3Location, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Key=Key,
            **kwargs
        )
        super(S3Location, self).__init__(**processed_kwargs)


class Output(troposphere.databrew.Output, Mixin):
    def __init__(self,
                 title=None,
                 Location=REQUIRED, # type: _S3Location
                 CompressionFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 Format=NOTHING, # type: Union[str, AWSHelperFn]
                 FormatOptions=NOTHING, # type: _OutputFormatOptions
                 Overwrite=NOTHING, # type: bool
                 PartitionColumns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Location=Location,
            CompressionFormat=CompressionFormat,
            Format=Format,
            FormatOptions=FormatOptions,
            Overwrite=Overwrite,
            PartitionColumns=PartitionColumns,
            **kwargs
        )
        super(Output, self).__init__(**processed_kwargs)


class Job(troposphere.databrew.Job, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 DatasetName=NOTHING, # type: Union[str, AWSHelperFn]
                 EncryptionKeyArn=NOTHING, # type: Union[str, AWSHelperFn]
                 EncryptionMode=NOTHING, # type: Union[str, AWSHelperFn]
                 JobSample=NOTHING, # type: dict
                 LogSubscription=NOTHING, # type: Union[str, AWSHelperFn]
                 MaxCapacity=NOTHING, # type: int
                 MaxRetries=NOTHING, # type: int
                 OutputLocation=NOTHING, # type: dict
                 Outputs=NOTHING, # type: List[_Output]
                 ProjectName=NOTHING, # type: Union[str, AWSHelperFn]
                 Recipe=NOTHING, # type: dict
                 Tags=NOTHING, # type: _Tags
                 Timeout=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            RoleArn=RoleArn,
            Type=Type,
            DatasetName=DatasetName,
            EncryptionKeyArn=EncryptionKeyArn,
            EncryptionMode=EncryptionMode,
            JobSample=JobSample,
            LogSubscription=LogSubscription,
            MaxCapacity=MaxCapacity,
            MaxRetries=MaxRetries,
            OutputLocation=OutputLocation,
            Outputs=Outputs,
            ProjectName=ProjectName,
            Recipe=Recipe,
            Tags=Tags,
            Timeout=Timeout,
            **kwargs
        )
        super(Job, self).__init__(**processed_kwargs)


class Project(troposphere.databrew.Project, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DatasetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RecipeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Sample=NOTHING, # type: dict
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DatasetName=DatasetName,
            Name=Name,
            RecipeName=RecipeName,
            RoleArn=RoleArn,
            Sample=Sample,
            Tags=Tags,
            **kwargs
        )
        super(Project, self).__init__(**processed_kwargs)


class DataCatalogInputDefinition(troposphere.databrew.DataCatalogInputDefinition, Mixin):
    def __init__(self,
                 title=None,
                 CatalogId=NOTHING, # type: Union[str, AWSHelperFn]
                 DatabaseName=NOTHING, # type: Union[str, AWSHelperFn]
                 TableName=NOTHING, # type: Union[str, AWSHelperFn]
                 TempDirectory=NOTHING, # type: _S3Location
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CatalogId=CatalogId,
            DatabaseName=DatabaseName,
            TableName=TableName,
            TempDirectory=TempDirectory,
            **kwargs
        )
        super(DataCatalogInputDefinition, self).__init__(**processed_kwargs)


class SecondaryInput(troposphere.databrew.SecondaryInput, Mixin):
    def __init__(self,
                 title=None,
                 DataCatalogInputDefinition=NOTHING, # type: _DataCatalogInputDefinition
                 S3InputDefinition=NOTHING, # type: _S3Location
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataCatalogInputDefinition=DataCatalogInputDefinition,
            S3InputDefinition=S3InputDefinition,
            **kwargs
        )
        super(SecondaryInput, self).__init__(**processed_kwargs)


class RecipeParameters(troposphere.databrew.RecipeParameters, Mixin):
    def __init__(self,
                 title=None,
                 AggregateFunction=NOTHING, # type: Union[str, AWSHelperFn]
                 Base=NOTHING, # type: Union[str, AWSHelperFn]
                 CaseStatement=NOTHING, # type: Union[str, AWSHelperFn]
                 CategoryMap=NOTHING, # type: Union[str, AWSHelperFn]
                 CharsToRemove=NOTHING, # type: Union[str, AWSHelperFn]
                 CollapseConsecutiveWhitespace=NOTHING, # type: Union[str, AWSHelperFn]
                 ColumnDataType=NOTHING, # type: Union[str, AWSHelperFn]
                 ColumnRange=NOTHING, # type: Union[str, AWSHelperFn]
                 Count=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomCharacters=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomStopWords=NOTHING, # type: Union[str, AWSHelperFn]
                 CustomValue=NOTHING, # type: Union[str, AWSHelperFn]
                 DatasetsColumns=NOTHING, # type: Union[str, AWSHelperFn]
                 DateAddValue=NOTHING, # type: Union[str, AWSHelperFn]
                 DateTimeFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 DateTimeParameters=NOTHING, # type: Union[str, AWSHelperFn]
                 DeleteOtherRows=NOTHING, # type: Union[str, AWSHelperFn]
                 Delimiter=NOTHING, # type: Union[str, AWSHelperFn]
                 EndPattern=NOTHING, # type: Union[str, AWSHelperFn]
                 EndPosition=NOTHING, # type: Union[str, AWSHelperFn]
                 EndValue=NOTHING, # type: Union[str, AWSHelperFn]
                 ExpandContractions=NOTHING, # type: Union[str, AWSHelperFn]
                 Exponent=NOTHING, # type: Union[str, AWSHelperFn]
                 FalseString=NOTHING, # type: Union[str, AWSHelperFn]
                 GroupByAggFunctionOptions=NOTHING, # type: Union[str, AWSHelperFn]
                 GroupByColumns=NOTHING, # type: Union[str, AWSHelperFn]
                 HiddenColumns=NOTHING, # type: Union[str, AWSHelperFn]
                 IgnoreCase=NOTHING, # type: Union[str, AWSHelperFn]
                 IncludeInSplit=NOTHING, # type: Union[str, AWSHelperFn]
                 Input=NOTHING, # type: dict
                 Interval=NOTHING, # type: Union[str, AWSHelperFn]
                 IsText=NOTHING, # type: Union[str, AWSHelperFn]
                 JoinKeys=NOTHING, # type: Union[str, AWSHelperFn]
                 JoinType=NOTHING, # type: Union[str, AWSHelperFn]
                 LeftColumns=NOTHING, # type: Union[str, AWSHelperFn]
                 Limit=NOTHING, # type: Union[str, AWSHelperFn]
                 LowerBound=NOTHING, # type: Union[str, AWSHelperFn]
                 MapType=NOTHING, # type: Union[str, AWSHelperFn]
                 ModeType=NOTHING, # type: Union[str, AWSHelperFn]
                 MultiLine=NOTHING, # type: bool
                 NumRows=NOTHING, # type: Union[str, AWSHelperFn]
                 NumRowsAfter=NOTHING, # type: Union[str, AWSHelperFn]
                 NumRowsBefore=NOTHING, # type: Union[str, AWSHelperFn]
                 OrderByColumn=NOTHING, # type: Union[str, AWSHelperFn]
                 OrderByColumns=NOTHING, # type: Union[str, AWSHelperFn]
                 Other=NOTHING, # type: Union[str, AWSHelperFn]
                 Pattern=NOTHING, # type: Union[str, AWSHelperFn]
                 PatternOption1=NOTHING, # type: Union[str, AWSHelperFn]
                 PatternOption2=NOTHING, # type: Union[str, AWSHelperFn]
                 PatternOptions=NOTHING, # type: Union[str, AWSHelperFn]
                 Period=NOTHING, # type: Union[str, AWSHelperFn]
                 Position=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveAllPunctuation=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveAllQuotes=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveAllWhitespace=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveCustomCharacters=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveCustomValue=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveLeadingAndTrailingPunctuation=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveLeadingAndTrailingQuotes=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveLeadingAndTrailingWhitespace=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveLetters=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveNumbers=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveSourceColumn=NOTHING, # type: Union[str, AWSHelperFn]
                 RemoveSpecialCharacters=NOTHING, # type: Union[str, AWSHelperFn]
                 RightColumns=NOTHING, # type: Union[str, AWSHelperFn]
                 SampleSize=NOTHING, # type: Union[str, AWSHelperFn]
                 SampleType=NOTHING, # type: Union[str, AWSHelperFn]
                 SecondInput=NOTHING, # type: Union[str, AWSHelperFn]
                 SecondaryInputs=NOTHING, # type: List[_SecondaryInput]
                 SheetIndexes=NOTHING, # type: List[_integer]
                 SheetNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 SourceColumn=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceColumn1=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceColumn2=NOTHING, # type: Union[str, AWSHelperFn]
                 SourceColumns=NOTHING, # type: Union[str, AWSHelperFn]
                 StartColumnIndex=NOTHING, # type: Union[str, AWSHelperFn]
                 StartPattern=NOTHING, # type: Union[str, AWSHelperFn]
                 StartPosition=NOTHING, # type: Union[str, AWSHelperFn]
                 StartValue=NOTHING, # type: Union[str, AWSHelperFn]
                 StemmingMode=NOTHING, # type: Union[str, AWSHelperFn]
                 StepCount=NOTHING, # type: Union[str, AWSHelperFn]
                 StepIndex=NOTHING, # type: Union[str, AWSHelperFn]
                 StopWordsMode=NOTHING, # type: Union[str, AWSHelperFn]
                 Strategy=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetColumn=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetColumnNames=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetDateFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetIndex=NOTHING, # type: Union[str, AWSHelperFn]
                 TimeZone=NOTHING, # type: Union[str, AWSHelperFn]
                 TokenizerPattern=NOTHING, # type: Union[str, AWSHelperFn]
                 TrueString=NOTHING, # type: Union[str, AWSHelperFn]
                 UdfLang=NOTHING, # type: Union[str, AWSHelperFn]
                 Units=NOTHING, # type: Union[str, AWSHelperFn]
                 UnpivotColumn=NOTHING, # type: Union[str, AWSHelperFn]
                 UpperBound=NOTHING, # type: Union[str, AWSHelperFn]
                 UseNewDataFrame=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 Value1=NOTHING, # type: Union[str, AWSHelperFn]
                 Value2=NOTHING, # type: Union[str, AWSHelperFn]
                 ValueColumn=NOTHING, # type: Union[str, AWSHelperFn]
                 ViewFrame=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AggregateFunction=AggregateFunction,
            Base=Base,
            CaseStatement=CaseStatement,
            CategoryMap=CategoryMap,
            CharsToRemove=CharsToRemove,
            CollapseConsecutiveWhitespace=CollapseConsecutiveWhitespace,
            ColumnDataType=ColumnDataType,
            ColumnRange=ColumnRange,
            Count=Count,
            CustomCharacters=CustomCharacters,
            CustomStopWords=CustomStopWords,
            CustomValue=CustomValue,
            DatasetsColumns=DatasetsColumns,
            DateAddValue=DateAddValue,
            DateTimeFormat=DateTimeFormat,
            DateTimeParameters=DateTimeParameters,
            DeleteOtherRows=DeleteOtherRows,
            Delimiter=Delimiter,
            EndPattern=EndPattern,
            EndPosition=EndPosition,
            EndValue=EndValue,
            ExpandContractions=ExpandContractions,
            Exponent=Exponent,
            FalseString=FalseString,
            GroupByAggFunctionOptions=GroupByAggFunctionOptions,
            GroupByColumns=GroupByColumns,
            HiddenColumns=HiddenColumns,
            IgnoreCase=IgnoreCase,
            IncludeInSplit=IncludeInSplit,
            Input=Input,
            Interval=Interval,
            IsText=IsText,
            JoinKeys=JoinKeys,
            JoinType=JoinType,
            LeftColumns=LeftColumns,
            Limit=Limit,
            LowerBound=LowerBound,
            MapType=MapType,
            ModeType=ModeType,
            MultiLine=MultiLine,
            NumRows=NumRows,
            NumRowsAfter=NumRowsAfter,
            NumRowsBefore=NumRowsBefore,
            OrderByColumn=OrderByColumn,
            OrderByColumns=OrderByColumns,
            Other=Other,
            Pattern=Pattern,
            PatternOption1=PatternOption1,
            PatternOption2=PatternOption2,
            PatternOptions=PatternOptions,
            Period=Period,
            Position=Position,
            RemoveAllPunctuation=RemoveAllPunctuation,
            RemoveAllQuotes=RemoveAllQuotes,
            RemoveAllWhitespace=RemoveAllWhitespace,
            RemoveCustomCharacters=RemoveCustomCharacters,
            RemoveCustomValue=RemoveCustomValue,
            RemoveLeadingAndTrailingPunctuation=RemoveLeadingAndTrailingPunctuation,
            RemoveLeadingAndTrailingQuotes=RemoveLeadingAndTrailingQuotes,
            RemoveLeadingAndTrailingWhitespace=RemoveLeadingAndTrailingWhitespace,
            RemoveLetters=RemoveLetters,
            RemoveNumbers=RemoveNumbers,
            RemoveSourceColumn=RemoveSourceColumn,
            RemoveSpecialCharacters=RemoveSpecialCharacters,
            RightColumns=RightColumns,
            SampleSize=SampleSize,
            SampleType=SampleType,
            SecondInput=SecondInput,
            SecondaryInputs=SecondaryInputs,
            SheetIndexes=SheetIndexes,
            SheetNames=SheetNames,
            SourceColumn=SourceColumn,
            SourceColumn1=SourceColumn1,
            SourceColumn2=SourceColumn2,
            SourceColumns=SourceColumns,
            StartColumnIndex=StartColumnIndex,
            StartPattern=StartPattern,
            StartPosition=StartPosition,
            StartValue=StartValue,
            StemmingMode=StemmingMode,
            StepCount=StepCount,
            StepIndex=StepIndex,
            StopWordsMode=StopWordsMode,
            Strategy=Strategy,
            TargetColumn=TargetColumn,
            TargetColumnNames=TargetColumnNames,
            TargetDateFormat=TargetDateFormat,
            TargetIndex=TargetIndex,
            TimeZone=TimeZone,
            TokenizerPattern=TokenizerPattern,
            TrueString=TrueString,
            UdfLang=UdfLang,
            Units=Units,
            UnpivotColumn=UnpivotColumn,
            UpperBound=UpperBound,
            UseNewDataFrame=UseNewDataFrame,
            Value=Value,
            Value1=Value1,
            Value2=Value2,
            ValueColumn=ValueColumn,
            ViewFrame=ViewFrame,
            **kwargs
        )
        super(RecipeParameters, self).__init__(**processed_kwargs)


class Action(troposphere.databrew.Action, Mixin):
    def __init__(self,
                 title=None,
                 Operation=REQUIRED, # type: Union[str, AWSHelperFn]
                 Parameters=NOTHING, # type: _RecipeParameters
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Operation=Operation,
            Parameters=Parameters,
            **kwargs
        )
        super(Action, self).__init__(**processed_kwargs)


class ConditionExpression(troposphere.databrew.ConditionExpression, Mixin):
    def __init__(self,
                 title=None,
                 Condition=REQUIRED, # type: Union[str, AWSHelperFn]
                 TargetColumn=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Condition=Condition,
            TargetColumn=TargetColumn,
            Value=Value,
            **kwargs
        )
        super(ConditionExpression, self).__init__(**processed_kwargs)


class RecipeStep(troposphere.databrew.RecipeStep, Mixin):
    def __init__(self,
                 title=None,
                 Action=REQUIRED, # type: _Action
                 ConditionExpressions=NOTHING, # type: List[_ConditionExpression]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Action=Action,
            ConditionExpressions=ConditionExpressions,
            **kwargs
        )
        super(RecipeStep, self).__init__(**processed_kwargs)


class Recipe(troposphere.databrew.Recipe, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Steps=REQUIRED, # type: List[_RecipeStep]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Name=Name,
            Steps=Steps,
            Description=Description,
            Tags=Tags,
            **kwargs
        )
        super(Recipe, self).__init__(**processed_kwargs)


class Schedule(troposphere.databrew.Schedule, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 CronExpression=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 JobNames=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            CronExpression=CronExpression,
            Name=Name,
            JobNames=JobNames,
            Tags=Tags,
            **kwargs
        )
        super(Schedule, self).__init__(**processed_kwargs)
