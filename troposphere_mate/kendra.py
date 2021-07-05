# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.kendra

from troposphere.kendra import (
    AccessControlListConfiguration as _AccessControlListConfiguration,
    AclConfiguration as _AclConfiguration,
    CapacityUnitsConfiguration as _CapacityUnitsConfiguration,
    ChangeDetectingColumns as _ChangeDetectingColumns,
    ColumnConfiguration as _ColumnConfiguration,
    ConfluenceAttachmentConfiguration as _ConfluenceAttachmentConfiguration,
    ConfluenceAttachmentFieldMappingsList as _ConfluenceAttachmentFieldMappingsList,
    ConfluenceAttachmentToIndexFieldMapping as _ConfluenceAttachmentToIndexFieldMapping,
    ConfluenceBlogConfiguration as _ConfluenceBlogConfiguration,
    ConfluenceBlogFieldMappingsList as _ConfluenceBlogFieldMappingsList,
    ConfluenceBlogToIndexFieldMapping as _ConfluenceBlogToIndexFieldMapping,
    ConfluenceConfiguration as _ConfluenceConfiguration,
    ConfluencePageConfiguration as _ConfluencePageConfiguration,
    ConfluencePageFieldMappingsList as _ConfluencePageFieldMappingsList,
    ConfluencePageToIndexFieldMapping as _ConfluencePageToIndexFieldMapping,
    ConfluenceSpaceConfiguration as _ConfluenceSpaceConfiguration,
    ConfluenceSpaceFieldMappingsList as _ConfluenceSpaceFieldMappingsList,
    ConfluenceSpaceList as _ConfluenceSpaceList,
    ConfluenceSpaceToIndexFieldMapping as _ConfluenceSpaceToIndexFieldMapping,
    ConnectionConfiguration as _ConnectionConfiguration,
    DataSourceConfiguration as _DataSourceConfiguration,
    DataSourceInclusionsExclusionsStrings as _DataSourceInclusionsExclusionsStrings,
    DataSourceToIndexFieldMapping as _DataSourceToIndexFieldMapping,
    DataSourceToIndexFieldMappingList as _DataSourceToIndexFieldMappingList,
    DataSourceVpcConfiguration as _DataSourceVpcConfiguration,
    DatabaseConfiguration as _DatabaseConfiguration,
    DocumentMetadataConfiguration as _DocumentMetadataConfiguration,
    DocumentsMetadataConfiguration as _DocumentsMetadataConfiguration,
    ExcludeMimeTypesList as _ExcludeMimeTypesList,
    ExcludeSharedDrivesList as _ExcludeSharedDrivesList,
    ExcludeUserAccountsList as _ExcludeUserAccountsList,
    GoogleDriveConfiguration as _GoogleDriveConfiguration,
    JsonTokenTypeConfiguration as _JsonTokenTypeConfiguration,
    JwtTokenTypeConfiguration as _JwtTokenTypeConfiguration,
    OneDriveConfiguration as _OneDriveConfiguration,
    OneDriveUserList as _OneDriveUserList,
    OneDriveUsers as _OneDriveUsers,
    Relevance as _Relevance,
    S3DataSourceConfiguration as _S3DataSourceConfiguration,
    S3Path as _S3Path,
    SalesforceChatterFeedConfiguration as _SalesforceChatterFeedConfiguration,
    SalesforceChatterFeedIncludeFilterTypes as _SalesforceChatterFeedIncludeFilterTypes,
    SalesforceConfiguration as _SalesforceConfiguration,
    SalesforceCustomKnowledgeArticleTypeConfiguration as _SalesforceCustomKnowledgeArticleTypeConfiguration,
    SalesforceCustomKnowledgeArticleTypeConfigurationList as _SalesforceCustomKnowledgeArticleTypeConfigurationList,
    SalesforceKnowledgeArticleConfiguration as _SalesforceKnowledgeArticleConfiguration,
    SalesforceKnowledgeArticleStateList as _SalesforceKnowledgeArticleStateList,
    SalesforceStandardKnowledgeArticleTypeConfiguration as _SalesforceStandardKnowledgeArticleTypeConfiguration,
    SalesforceStandardObjectAttachmentConfiguration as _SalesforceStandardObjectAttachmentConfiguration,
    SalesforceStandardObjectConfiguration as _SalesforceStandardObjectConfiguration,
    SalesforceStandardObjectConfigurationList as _SalesforceStandardObjectConfigurationList,
    Search as _Search,
    ServerSideEncryptionConfiguration as _ServerSideEncryptionConfiguration,
    ServiceNowConfiguration as _ServiceNowConfiguration,
    ServiceNowKnowledgeArticleConfiguration as _ServiceNowKnowledgeArticleConfiguration,
    ServiceNowServiceCatalogConfiguration as _ServiceNowServiceCatalogConfiguration,
    SharePointConfiguration as _SharePointConfiguration,
    SqlConfiguration as _SqlConfiguration,
    Tags as _Tags,
    UserTokenConfiguration as _UserTokenConfiguration,
    ValueImportanceItem as _ValueImportanceItem,
    ValueImportanceItems as _ValueImportanceItems,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class ConfluenceAttachmentToIndexFieldMapping(troposphere.kendra.ConfluenceAttachmentToIndexFieldMapping, Mixin):
    def __init__(self,
                 title=None,
                 DataSourceFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 IndexFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DateFieldFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataSourceFieldName=DataSourceFieldName,
            IndexFieldName=IndexFieldName,
            DateFieldFormat=DateFieldFormat,
            **kwargs
        )
        super(ConfluenceAttachmentToIndexFieldMapping, self).__init__(**processed_kwargs)


class ConfluenceAttachmentFieldMappingsList(troposphere.kendra.ConfluenceAttachmentFieldMappingsList, Mixin):
    def __init__(self,
                 title=None,
                 ConfluenceAttachmentFieldMappingsList=NOTHING, # type: List[_ConfluenceAttachmentToIndexFieldMapping]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfluenceAttachmentFieldMappingsList=ConfluenceAttachmentFieldMappingsList,
            **kwargs
        )
        super(ConfluenceAttachmentFieldMappingsList, self).__init__(**processed_kwargs)


class ConfluenceAttachmentConfiguration(troposphere.kendra.ConfluenceAttachmentConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AttachmentFieldMappings=NOTHING, # type: _ConfluenceAttachmentFieldMappingsList
                 CrawlAttachments=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AttachmentFieldMappings=AttachmentFieldMappings,
            CrawlAttachments=CrawlAttachments,
            **kwargs
        )
        super(ConfluenceAttachmentConfiguration, self).__init__(**processed_kwargs)


class ConfluenceBlogToIndexFieldMapping(troposphere.kendra.ConfluenceBlogToIndexFieldMapping, Mixin):
    def __init__(self,
                 title=None,
                 DataSourceFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 IndexFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DateFieldFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataSourceFieldName=DataSourceFieldName,
            IndexFieldName=IndexFieldName,
            DateFieldFormat=DateFieldFormat,
            **kwargs
        )
        super(ConfluenceBlogToIndexFieldMapping, self).__init__(**processed_kwargs)


class ConfluenceBlogFieldMappingsList(troposphere.kendra.ConfluenceBlogFieldMappingsList, Mixin):
    def __init__(self,
                 title=None,
                 ConfluenceBlogFieldMappingsList=NOTHING, # type: List[_ConfluenceBlogToIndexFieldMapping]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfluenceBlogFieldMappingsList=ConfluenceBlogFieldMappingsList,
            **kwargs
        )
        super(ConfluenceBlogFieldMappingsList, self).__init__(**processed_kwargs)


class ConfluenceBlogConfiguration(troposphere.kendra.ConfluenceBlogConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 BlogFieldMappings=NOTHING, # type: _ConfluenceBlogFieldMappingsList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BlogFieldMappings=BlogFieldMappings,
            **kwargs
        )
        super(ConfluenceBlogConfiguration, self).__init__(**processed_kwargs)


class ConfluencePageToIndexFieldMapping(troposphere.kendra.ConfluencePageToIndexFieldMapping, Mixin):
    def __init__(self,
                 title=None,
                 DataSourceFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 IndexFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DateFieldFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataSourceFieldName=DataSourceFieldName,
            IndexFieldName=IndexFieldName,
            DateFieldFormat=DateFieldFormat,
            **kwargs
        )
        super(ConfluencePageToIndexFieldMapping, self).__init__(**processed_kwargs)


class ConfluencePageFieldMappingsList(troposphere.kendra.ConfluencePageFieldMappingsList, Mixin):
    def __init__(self,
                 title=None,
                 ConfluencePageFieldMappingsList=NOTHING, # type: List[_ConfluencePageToIndexFieldMapping]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfluencePageFieldMappingsList=ConfluencePageFieldMappingsList,
            **kwargs
        )
        super(ConfluencePageFieldMappingsList, self).__init__(**processed_kwargs)


class ConfluencePageConfiguration(troposphere.kendra.ConfluencePageConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 PageFieldMappings=NOTHING, # type: _ConfluencePageFieldMappingsList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PageFieldMappings=PageFieldMappings,
            **kwargs
        )
        super(ConfluencePageConfiguration, self).__init__(**processed_kwargs)


class ConfluenceSpaceToIndexFieldMapping(troposphere.kendra.ConfluenceSpaceToIndexFieldMapping, Mixin):
    def __init__(self,
                 title=None,
                 DataSourceFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 IndexFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DateFieldFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataSourceFieldName=DataSourceFieldName,
            IndexFieldName=IndexFieldName,
            DateFieldFormat=DateFieldFormat,
            **kwargs
        )
        super(ConfluenceSpaceToIndexFieldMapping, self).__init__(**processed_kwargs)


class ConfluenceSpaceFieldMappingsList(troposphere.kendra.ConfluenceSpaceFieldMappingsList, Mixin):
    def __init__(self,
                 title=None,
                 ConfluenceSpaceFieldMappingsList=NOTHING, # type: List[_ConfluenceSpaceToIndexFieldMapping]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfluenceSpaceFieldMappingsList=ConfluenceSpaceFieldMappingsList,
            **kwargs
        )
        super(ConfluenceSpaceFieldMappingsList, self).__init__(**processed_kwargs)


class ConfluenceSpaceList(troposphere.kendra.ConfluenceSpaceList, Mixin):
    def __init__(self,
                 title=None,
                 ConfluenceSpaceList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfluenceSpaceList=ConfluenceSpaceList,
            **kwargs
        )
        super(ConfluenceSpaceList, self).__init__(**processed_kwargs)


class ConfluenceSpaceConfiguration(troposphere.kendra.ConfluenceSpaceConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 CrawlArchivedSpaces=NOTHING, # type: bool
                 CrawlPersonalSpaces=NOTHING, # type: bool
                 ExcludeSpaces=NOTHING, # type: _ConfluenceSpaceList
                 IncludeSpaces=NOTHING, # type: _ConfluenceSpaceList
                 SpaceFieldMappings=NOTHING, # type: _ConfluenceSpaceFieldMappingsList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CrawlArchivedSpaces=CrawlArchivedSpaces,
            CrawlPersonalSpaces=CrawlPersonalSpaces,
            ExcludeSpaces=ExcludeSpaces,
            IncludeSpaces=IncludeSpaces,
            SpaceFieldMappings=SpaceFieldMappings,
            **kwargs
        )
        super(ConfluenceSpaceConfiguration, self).__init__(**processed_kwargs)


class DataSourceInclusionsExclusionsStrings(troposphere.kendra.DataSourceInclusionsExclusionsStrings, Mixin):
    def __init__(self,
                 title=None,
                 DataSourceInclusionsExclusionsStrings=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataSourceInclusionsExclusionsStrings=DataSourceInclusionsExclusionsStrings,
            **kwargs
        )
        super(DataSourceInclusionsExclusionsStrings, self).__init__(**processed_kwargs)


class DataSourceVpcConfiguration(troposphere.kendra.DataSourceVpcConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SecurityGroupIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 SubnetIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecurityGroupIds=SecurityGroupIds,
            SubnetIds=SubnetIds,
            **kwargs
        )
        super(DataSourceVpcConfiguration, self).__init__(**processed_kwargs)


class ConfluenceConfiguration(troposphere.kendra.ConfluenceConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SecretArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServerUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 Version=REQUIRED, # type: Union[str, AWSHelperFn]
                 AttachmentConfiguration=NOTHING, # type: _ConfluenceAttachmentConfiguration
                 BlogConfiguration=NOTHING, # type: _ConfluenceBlogConfiguration
                 ExclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 InclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 PageConfiguration=NOTHING, # type: _ConfluencePageConfiguration
                 SpaceConfiguration=NOTHING, # type: _ConfluenceSpaceConfiguration
                 VpcConfiguration=NOTHING, # type: _DataSourceVpcConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretArn=SecretArn,
            ServerUrl=ServerUrl,
            Version=Version,
            AttachmentConfiguration=AttachmentConfiguration,
            BlogConfiguration=BlogConfiguration,
            ExclusionPatterns=ExclusionPatterns,
            InclusionPatterns=InclusionPatterns,
            PageConfiguration=PageConfiguration,
            SpaceConfiguration=SpaceConfiguration,
            VpcConfiguration=VpcConfiguration,
            **kwargs
        )
        super(ConfluenceConfiguration, self).__init__(**processed_kwargs)


class AclConfiguration(troposphere.kendra.AclConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 AllowedGroupsColumnName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            AllowedGroupsColumnName=AllowedGroupsColumnName,
            **kwargs
        )
        super(AclConfiguration, self).__init__(**processed_kwargs)


class ChangeDetectingColumns(troposphere.kendra.ChangeDetectingColumns, Mixin):
    def __init__(self,
                 title=None,
                 ChangeDetectingColumns=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ChangeDetectingColumns=ChangeDetectingColumns,
            **kwargs
        )
        super(ChangeDetectingColumns, self).__init__(**processed_kwargs)


class DataSourceToIndexFieldMapping(troposphere.kendra.DataSourceToIndexFieldMapping, Mixin):
    def __init__(self,
                 title=None,
                 DataSourceFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 IndexFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DateFieldFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataSourceFieldName=DataSourceFieldName,
            IndexFieldName=IndexFieldName,
            DateFieldFormat=DateFieldFormat,
            **kwargs
        )
        super(DataSourceToIndexFieldMapping, self).__init__(**processed_kwargs)


class DataSourceToIndexFieldMappingList(troposphere.kendra.DataSourceToIndexFieldMappingList, Mixin):
    def __init__(self,
                 title=None,
                 DataSourceToIndexFieldMappingList=NOTHING, # type: List[_DataSourceToIndexFieldMapping]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataSourceToIndexFieldMappingList=DataSourceToIndexFieldMappingList,
            **kwargs
        )
        super(DataSourceToIndexFieldMappingList, self).__init__(**processed_kwargs)


class ColumnConfiguration(troposphere.kendra.ColumnConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ChangeDetectingColumns=REQUIRED, # type: _ChangeDetectingColumns
                 DocumentDataColumnName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DocumentIdColumnName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DocumentTitleColumnName=NOTHING, # type: Union[str, AWSHelperFn]
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ChangeDetectingColumns=ChangeDetectingColumns,
            DocumentDataColumnName=DocumentDataColumnName,
            DocumentIdColumnName=DocumentIdColumnName,
            DocumentTitleColumnName=DocumentTitleColumnName,
            FieldMappings=FieldMappings,
            **kwargs
        )
        super(ColumnConfiguration, self).__init__(**processed_kwargs)


class ConnectionConfiguration(troposphere.kendra.ConnectionConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DatabaseHost=REQUIRED, # type: Union[str, AWSHelperFn]
                 DatabaseName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DatabasePort=REQUIRED, # type: int
                 SecretArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TableName=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DatabaseHost=DatabaseHost,
            DatabaseName=DatabaseName,
            DatabasePort=DatabasePort,
            SecretArn=SecretArn,
            TableName=TableName,
            **kwargs
        )
        super(ConnectionConfiguration, self).__init__(**processed_kwargs)


class SqlConfiguration(troposphere.kendra.SqlConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 QueryIdentifiersEnclosingOption=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            QueryIdentifiersEnclosingOption=QueryIdentifiersEnclosingOption,
            **kwargs
        )
        super(SqlConfiguration, self).__init__(**processed_kwargs)


class DatabaseConfiguration(troposphere.kendra.DatabaseConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ColumnConfiguration=REQUIRED, # type: _ColumnConfiguration
                 ConnectionConfiguration=REQUIRED, # type: _ConnectionConfiguration
                 DatabaseEngineType=REQUIRED, # type: Union[str, AWSHelperFn]
                 AclConfiguration=NOTHING, # type: _AclConfiguration
                 SqlConfiguration=NOTHING, # type: _SqlConfiguration
                 VpcConfiguration=NOTHING, # type: _DataSourceVpcConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ColumnConfiguration=ColumnConfiguration,
            ConnectionConfiguration=ConnectionConfiguration,
            DatabaseEngineType=DatabaseEngineType,
            AclConfiguration=AclConfiguration,
            SqlConfiguration=SqlConfiguration,
            VpcConfiguration=VpcConfiguration,
            **kwargs
        )
        super(DatabaseConfiguration, self).__init__(**processed_kwargs)


class ExcludeMimeTypesList(troposphere.kendra.ExcludeMimeTypesList, Mixin):
    def __init__(self,
                 title=None,
                 ExcludeMimeTypesList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExcludeMimeTypesList=ExcludeMimeTypesList,
            **kwargs
        )
        super(ExcludeMimeTypesList, self).__init__(**processed_kwargs)


class ExcludeSharedDrivesList(troposphere.kendra.ExcludeSharedDrivesList, Mixin):
    def __init__(self,
                 title=None,
                 ExcludeSharedDrivesList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExcludeSharedDrivesList=ExcludeSharedDrivesList,
            **kwargs
        )
        super(ExcludeSharedDrivesList, self).__init__(**processed_kwargs)


class ExcludeUserAccountsList(troposphere.kendra.ExcludeUserAccountsList, Mixin):
    def __init__(self,
                 title=None,
                 ExcludeUserAccountsList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExcludeUserAccountsList=ExcludeUserAccountsList,
            **kwargs
        )
        super(ExcludeUserAccountsList, self).__init__(**processed_kwargs)


class GoogleDriveConfiguration(troposphere.kendra.GoogleDriveConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SecretArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ExcludeMimeTypes=NOTHING, # type: _ExcludeMimeTypesList
                 ExcludeSharedDrives=NOTHING, # type: _ExcludeSharedDrivesList
                 ExcludeUserAccounts=NOTHING, # type: _ExcludeUserAccountsList
                 ExclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 InclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretArn=SecretArn,
            ExcludeMimeTypes=ExcludeMimeTypes,
            ExcludeSharedDrives=ExcludeSharedDrives,
            ExcludeUserAccounts=ExcludeUserAccounts,
            ExclusionPatterns=ExclusionPatterns,
            FieldMappings=FieldMappings,
            InclusionPatterns=InclusionPatterns,
            **kwargs
        )
        super(GoogleDriveConfiguration, self).__init__(**processed_kwargs)


class OneDriveUserList(troposphere.kendra.OneDriveUserList, Mixin):
    def __init__(self,
                 title=None,
                 OneDriveUserList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OneDriveUserList=OneDriveUserList,
            **kwargs
        )
        super(OneDriveUserList, self).__init__(**processed_kwargs)


class S3Path(troposphere.kendra.S3Path, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 Key=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            Key=Key,
            **kwargs
        )
        super(S3Path, self).__init__(**processed_kwargs)


class OneDriveUsers(troposphere.kendra.OneDriveUsers, Mixin):
    def __init__(self,
                 title=None,
                 OneDriveUserList=NOTHING, # type: _OneDriveUserList
                 OneDriveUserS3Path=NOTHING, # type: _S3Path
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OneDriveUserList=OneDriveUserList,
            OneDriveUserS3Path=OneDriveUserS3Path,
            **kwargs
        )
        super(OneDriveUsers, self).__init__(**processed_kwargs)


class OneDriveConfiguration(troposphere.kendra.OneDriveConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 OneDriveUsers=REQUIRED, # type: _OneDriveUsers
                 SecretArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 TenantDomain=REQUIRED, # type: Union[str, AWSHelperFn]
                 DisableLocalGroups=NOTHING, # type: bool
                 ExclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 InclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            OneDriveUsers=OneDriveUsers,
            SecretArn=SecretArn,
            TenantDomain=TenantDomain,
            DisableLocalGroups=DisableLocalGroups,
            ExclusionPatterns=ExclusionPatterns,
            FieldMappings=FieldMappings,
            InclusionPatterns=InclusionPatterns,
            **kwargs
        )
        super(OneDriveConfiguration, self).__init__(**processed_kwargs)


class AccessControlListConfiguration(troposphere.kendra.AccessControlListConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 KeyPath=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            KeyPath=KeyPath,
            **kwargs
        )
        super(AccessControlListConfiguration, self).__init__(**processed_kwargs)


class DocumentsMetadataConfiguration(troposphere.kendra.DocumentsMetadataConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 S3Prefix=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            S3Prefix=S3Prefix,
            **kwargs
        )
        super(DocumentsMetadataConfiguration, self).__init__(**processed_kwargs)


class S3DataSourceConfiguration(troposphere.kendra.S3DataSourceConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 BucketName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessControlListConfiguration=NOTHING, # type: _AccessControlListConfiguration
                 DocumentsMetadataConfiguration=NOTHING, # type: _DocumentsMetadataConfiguration
                 ExclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 InclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 InclusionPrefixes=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            BucketName=BucketName,
            AccessControlListConfiguration=AccessControlListConfiguration,
            DocumentsMetadataConfiguration=DocumentsMetadataConfiguration,
            ExclusionPatterns=ExclusionPatterns,
            InclusionPatterns=InclusionPatterns,
            InclusionPrefixes=InclusionPrefixes,
            **kwargs
        )
        super(S3DataSourceConfiguration, self).__init__(**processed_kwargs)


class SalesforceChatterFeedIncludeFilterTypes(troposphere.kendra.SalesforceChatterFeedIncludeFilterTypes, Mixin):
    def __init__(self,
                 title=None,
                 SalesforceChatterFeedIncludeFilterTypes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SalesforceChatterFeedIncludeFilterTypes=SalesforceChatterFeedIncludeFilterTypes,
            **kwargs
        )
        super(SalesforceChatterFeedIncludeFilterTypes, self).__init__(**processed_kwargs)


class SalesforceChatterFeedConfiguration(troposphere.kendra.SalesforceChatterFeedConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DocumentDataFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DocumentTitleFieldName=NOTHING, # type: Union[str, AWSHelperFn]
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 IncludeFilterTypes=NOTHING, # type: _SalesforceChatterFeedIncludeFilterTypes
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DocumentDataFieldName=DocumentDataFieldName,
            DocumentTitleFieldName=DocumentTitleFieldName,
            FieldMappings=FieldMappings,
            IncludeFilterTypes=IncludeFilterTypes,
            **kwargs
        )
        super(SalesforceChatterFeedConfiguration, self).__init__(**processed_kwargs)


class SalesforceCustomKnowledgeArticleTypeConfiguration(troposphere.kendra.SalesforceCustomKnowledgeArticleTypeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DocumentDataFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 DocumentTitleFieldName=NOTHING, # type: Union[str, AWSHelperFn]
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DocumentDataFieldName=DocumentDataFieldName,
            Name=Name,
            DocumentTitleFieldName=DocumentTitleFieldName,
            FieldMappings=FieldMappings,
            **kwargs
        )
        super(SalesforceCustomKnowledgeArticleTypeConfiguration, self).__init__(**processed_kwargs)


class SalesforceCustomKnowledgeArticleTypeConfigurationList(troposphere.kendra.SalesforceCustomKnowledgeArticleTypeConfigurationList, Mixin):
    def __init__(self,
                 title=None,
                 SalesforceCustomKnowledgeArticleTypeConfigurationList=NOTHING, # type: List[_SalesforceCustomKnowledgeArticleTypeConfiguration]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SalesforceCustomKnowledgeArticleTypeConfigurationList=SalesforceCustomKnowledgeArticleTypeConfigurationList,
            **kwargs
        )
        super(SalesforceCustomKnowledgeArticleTypeConfigurationList, self).__init__(**processed_kwargs)


class SalesforceKnowledgeArticleStateList(troposphere.kendra.SalesforceKnowledgeArticleStateList, Mixin):
    def __init__(self,
                 title=None,
                 SalesforceKnowledgeArticleStateList=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SalesforceKnowledgeArticleStateList=SalesforceKnowledgeArticleStateList,
            **kwargs
        )
        super(SalesforceKnowledgeArticleStateList, self).__init__(**processed_kwargs)


class SalesforceStandardKnowledgeArticleTypeConfiguration(troposphere.kendra.SalesforceStandardKnowledgeArticleTypeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DocumentDataFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 DocumentTitleFieldName=NOTHING, # type: Union[str, AWSHelperFn]
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DocumentDataFieldName=DocumentDataFieldName,
            DocumentTitleFieldName=DocumentTitleFieldName,
            FieldMappings=FieldMappings,
            **kwargs
        )
        super(SalesforceStandardKnowledgeArticleTypeConfiguration, self).__init__(**processed_kwargs)


class SalesforceKnowledgeArticleConfiguration(troposphere.kendra.SalesforceKnowledgeArticleConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 IncludedStates=REQUIRED, # type: _SalesforceKnowledgeArticleStateList
                 CustomKnowledgeArticleTypeConfigurations=NOTHING, # type: _SalesforceCustomKnowledgeArticleTypeConfigurationList
                 StandardKnowledgeArticleTypeConfiguration=NOTHING, # type: _SalesforceStandardKnowledgeArticleTypeConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IncludedStates=IncludedStates,
            CustomKnowledgeArticleTypeConfigurations=CustomKnowledgeArticleTypeConfigurations,
            StandardKnowledgeArticleTypeConfiguration=StandardKnowledgeArticleTypeConfiguration,
            **kwargs
        )
        super(SalesforceKnowledgeArticleConfiguration, self).__init__(**processed_kwargs)


class SalesforceStandardObjectAttachmentConfiguration(troposphere.kendra.SalesforceStandardObjectAttachmentConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DocumentTitleFieldName=NOTHING, # type: Union[str, AWSHelperFn]
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DocumentTitleFieldName=DocumentTitleFieldName,
            FieldMappings=FieldMappings,
            **kwargs
        )
        super(SalesforceStandardObjectAttachmentConfiguration, self).__init__(**processed_kwargs)


class SalesforceStandardObjectConfiguration(troposphere.kendra.SalesforceStandardObjectConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DocumentDataFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 DocumentTitleFieldName=NOTHING, # type: Union[str, AWSHelperFn]
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DocumentDataFieldName=DocumentDataFieldName,
            Name=Name,
            DocumentTitleFieldName=DocumentTitleFieldName,
            FieldMappings=FieldMappings,
            **kwargs
        )
        super(SalesforceStandardObjectConfiguration, self).__init__(**processed_kwargs)


class SalesforceStandardObjectConfigurationList(troposphere.kendra.SalesforceStandardObjectConfigurationList, Mixin):
    def __init__(self,
                 title=None,
                 SalesforceStandardObjectConfigurationList=NOTHING, # type: List[_SalesforceStandardObjectConfiguration]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SalesforceStandardObjectConfigurationList=SalesforceStandardObjectConfigurationList,
            **kwargs
        )
        super(SalesforceStandardObjectConfigurationList, self).__init__(**processed_kwargs)


class SalesforceConfiguration(troposphere.kendra.SalesforceConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SecretArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServerUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 ChatterFeedConfiguration=NOTHING, # type: _SalesforceChatterFeedConfiguration
                 CrawlAttachments=NOTHING, # type: bool
                 ExcludeAttachmentFilePatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 IncludeAttachmentFilePatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 KnowledgeArticleConfiguration=NOTHING, # type: _SalesforceKnowledgeArticleConfiguration
                 StandardObjectAttachmentConfiguration=NOTHING, # type: _SalesforceStandardObjectAttachmentConfiguration
                 StandardObjectConfigurations=NOTHING, # type: _SalesforceStandardObjectConfigurationList
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretArn=SecretArn,
            ServerUrl=ServerUrl,
            ChatterFeedConfiguration=ChatterFeedConfiguration,
            CrawlAttachments=CrawlAttachments,
            ExcludeAttachmentFilePatterns=ExcludeAttachmentFilePatterns,
            IncludeAttachmentFilePatterns=IncludeAttachmentFilePatterns,
            KnowledgeArticleConfiguration=KnowledgeArticleConfiguration,
            StandardObjectAttachmentConfiguration=StandardObjectAttachmentConfiguration,
            StandardObjectConfigurations=StandardObjectConfigurations,
            **kwargs
        )
        super(SalesforceConfiguration, self).__init__(**processed_kwargs)


class ServiceNowKnowledgeArticleConfiguration(troposphere.kendra.ServiceNowKnowledgeArticleConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DocumentDataFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CrawlAttachments=NOTHING, # type: bool
                 DocumentTitleFieldName=NOTHING, # type: Union[str, AWSHelperFn]
                 ExcludeAttachmentFilePatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 IncludeAttachmentFilePatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DocumentDataFieldName=DocumentDataFieldName,
            CrawlAttachments=CrawlAttachments,
            DocumentTitleFieldName=DocumentTitleFieldName,
            ExcludeAttachmentFilePatterns=ExcludeAttachmentFilePatterns,
            FieldMappings=FieldMappings,
            IncludeAttachmentFilePatterns=IncludeAttachmentFilePatterns,
            **kwargs
        )
        super(ServiceNowKnowledgeArticleConfiguration, self).__init__(**processed_kwargs)


class ServiceNowServiceCatalogConfiguration(troposphere.kendra.ServiceNowServiceCatalogConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 DocumentDataFieldName=REQUIRED, # type: Union[str, AWSHelperFn]
                 CrawlAttachments=NOTHING, # type: bool
                 DocumentTitleFieldName=NOTHING, # type: Union[str, AWSHelperFn]
                 ExcludeAttachmentFilePatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 IncludeAttachmentFilePatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DocumentDataFieldName=DocumentDataFieldName,
            CrawlAttachments=CrawlAttachments,
            DocumentTitleFieldName=DocumentTitleFieldName,
            ExcludeAttachmentFilePatterns=ExcludeAttachmentFilePatterns,
            FieldMappings=FieldMappings,
            IncludeAttachmentFilePatterns=IncludeAttachmentFilePatterns,
            **kwargs
        )
        super(ServiceNowServiceCatalogConfiguration, self).__init__(**processed_kwargs)


class ServiceNowConfiguration(troposphere.kendra.ServiceNowConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 HostUrl=REQUIRED, # type: Union[str, AWSHelperFn]
                 SecretArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServiceNowBuildVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 KnowledgeArticleConfiguration=NOTHING, # type: _ServiceNowKnowledgeArticleConfiguration
                 ServiceCatalogConfiguration=NOTHING, # type: _ServiceNowServiceCatalogConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            HostUrl=HostUrl,
            SecretArn=SecretArn,
            ServiceNowBuildVersion=ServiceNowBuildVersion,
            KnowledgeArticleConfiguration=KnowledgeArticleConfiguration,
            ServiceCatalogConfiguration=ServiceCatalogConfiguration,
            **kwargs
        )
        super(ServiceNowConfiguration, self).__init__(**processed_kwargs)


class SharePointConfiguration(troposphere.kendra.SharePointConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 SecretArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 SharePointVersion=REQUIRED, # type: Union[str, AWSHelperFn]
                 Urls=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 CrawlAttachments=NOTHING, # type: bool
                 DisableLocalGroups=NOTHING, # type: bool
                 DocumentTitleFieldName=NOTHING, # type: Union[str, AWSHelperFn]
                 ExclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 FieldMappings=NOTHING, # type: _DataSourceToIndexFieldMappingList
                 InclusionPatterns=NOTHING, # type: _DataSourceInclusionsExclusionsStrings
                 UseChangeLog=NOTHING, # type: bool
                 VpcConfiguration=NOTHING, # type: _DataSourceVpcConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecretArn=SecretArn,
            SharePointVersion=SharePointVersion,
            Urls=Urls,
            CrawlAttachments=CrawlAttachments,
            DisableLocalGroups=DisableLocalGroups,
            DocumentTitleFieldName=DocumentTitleFieldName,
            ExclusionPatterns=ExclusionPatterns,
            FieldMappings=FieldMappings,
            InclusionPatterns=InclusionPatterns,
            UseChangeLog=UseChangeLog,
            VpcConfiguration=VpcConfiguration,
            **kwargs
        )
        super(SharePointConfiguration, self).__init__(**processed_kwargs)


class DataSourceConfiguration(troposphere.kendra.DataSourceConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 ConfluenceConfiguration=NOTHING, # type: _ConfluenceConfiguration
                 DatabaseConfiguration=NOTHING, # type: _DatabaseConfiguration
                 GoogleDriveConfiguration=NOTHING, # type: _GoogleDriveConfiguration
                 OneDriveConfiguration=NOTHING, # type: _OneDriveConfiguration
                 S3Configuration=NOTHING, # type: _S3DataSourceConfiguration
                 SalesforceConfiguration=NOTHING, # type: _SalesforceConfiguration
                 ServiceNowConfiguration=NOTHING, # type: _ServiceNowConfiguration
                 SharePointConfiguration=NOTHING, # type: _SharePointConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ConfluenceConfiguration=ConfluenceConfiguration,
            DatabaseConfiguration=DatabaseConfiguration,
            GoogleDriveConfiguration=GoogleDriveConfiguration,
            OneDriveConfiguration=OneDriveConfiguration,
            S3Configuration=S3Configuration,
            SalesforceConfiguration=SalesforceConfiguration,
            ServiceNowConfiguration=ServiceNowConfiguration,
            SharePointConfiguration=SharePointConfiguration,
            **kwargs
        )
        super(DataSourceConfiguration, self).__init__(**processed_kwargs)


class DataSource(troposphere.kendra.DataSource, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 IndexId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 DataSourceConfiguration=NOTHING, # type: _DataSourceConfiguration
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 RoleArn=NOTHING, # type: Union[str, AWSHelperFn]
                 Schedule=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            IndexId=IndexId,
            Name=Name,
            Type=Type,
            DataSourceConfiguration=DataSourceConfiguration,
            Description=Description,
            RoleArn=RoleArn,
            Schedule=Schedule,
            Tags=Tags,
            **kwargs
        )
        super(DataSource, self).__init__(**processed_kwargs)


class Faq(troposphere.kendra.Faq, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 IndexId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Path=REQUIRED, # type: _S3Path
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 FileFormat=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            IndexId=IndexId,
            Name=Name,
            RoleArn=RoleArn,
            S3Path=S3Path,
            Description=Description,
            FileFormat=FileFormat,
            Tags=Tags,
            **kwargs
        )
        super(Faq, self).__init__(**processed_kwargs)


class CapacityUnitsConfiguration(troposphere.kendra.CapacityUnitsConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 QueryCapacityUnits=REQUIRED, # type: int
                 StorageCapacityUnits=REQUIRED, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            QueryCapacityUnits=QueryCapacityUnits,
            StorageCapacityUnits=StorageCapacityUnits,
            **kwargs
        )
        super(CapacityUnitsConfiguration, self).__init__(**processed_kwargs)


class ValueImportanceItem(troposphere.kendra.ValueImportanceItem, Mixin):
    def __init__(self,
                 title=None,
                 Key=NOTHING, # type: Union[str, AWSHelperFn]
                 Value=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Key=Key,
            Value=Value,
            **kwargs
        )
        super(ValueImportanceItem, self).__init__(**processed_kwargs)


class ValueImportanceItems(troposphere.kendra.ValueImportanceItems, Mixin):
    def __init__(self,
                 title=None,
                 ValueImportanceItems=NOTHING, # type: List[_ValueImportanceItem]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ValueImportanceItems=ValueImportanceItems,
            **kwargs
        )
        super(ValueImportanceItems, self).__init__(**processed_kwargs)


class Relevance(troposphere.kendra.Relevance, Mixin):
    def __init__(self,
                 title=None,
                 Duration=NOTHING, # type: Union[str, AWSHelperFn]
                 Freshness=NOTHING, # type: bool
                 Importance=NOTHING, # type: int
                 RankOrder=NOTHING, # type: Union[str, AWSHelperFn]
                 ValueImportanceItems=NOTHING, # type: _ValueImportanceItems
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Duration=Duration,
            Freshness=Freshness,
            Importance=Importance,
            RankOrder=RankOrder,
            ValueImportanceItems=ValueImportanceItems,
            **kwargs
        )
        super(Relevance, self).__init__(**processed_kwargs)


class Search(troposphere.kendra.Search, Mixin):
    def __init__(self,
                 title=None,
                 Displayable=NOTHING, # type: bool
                 Facetable=NOTHING, # type: bool
                 Searchable=NOTHING, # type: bool
                 Sortable=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Displayable=Displayable,
            Facetable=Facetable,
            Searchable=Searchable,
            Sortable=Sortable,
            **kwargs
        )
        super(Search, self).__init__(**processed_kwargs)


class DocumentMetadataConfiguration(troposphere.kendra.DocumentMetadataConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Relevance=NOTHING, # type: _Relevance
                 Search=NOTHING, # type: _Search
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Type=Type,
            Relevance=Relevance,
            Search=Search,
            **kwargs
        )
        super(DocumentMetadataConfiguration, self).__init__(**processed_kwargs)


class ServerSideEncryptionConfiguration(troposphere.kendra.ServerSideEncryptionConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 KmsKeyId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            KmsKeyId=KmsKeyId,
            **kwargs
        )
        super(ServerSideEncryptionConfiguration, self).__init__(**processed_kwargs)


class JsonTokenTypeConfiguration(troposphere.kendra.JsonTokenTypeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 GroupAttributeField=REQUIRED, # type: Union[str, AWSHelperFn]
                 UserNameAttributeField=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GroupAttributeField=GroupAttributeField,
            UserNameAttributeField=UserNameAttributeField,
            **kwargs
        )
        super(JsonTokenTypeConfiguration, self).__init__(**processed_kwargs)


class JwtTokenTypeConfiguration(troposphere.kendra.JwtTokenTypeConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 KeyLocation=REQUIRED, # type: Union[str, AWSHelperFn]
                 ClaimRegex=NOTHING, # type: Union[str, AWSHelperFn]
                 GroupAttributeField=NOTHING, # type: Union[str, AWSHelperFn]
                 Issuer=NOTHING, # type: Union[str, AWSHelperFn]
                 SecretManagerArn=NOTHING, # type: Union[str, AWSHelperFn]
                 URL=NOTHING, # type: Union[str, AWSHelperFn]
                 UserNameAttributeField=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            KeyLocation=KeyLocation,
            ClaimRegex=ClaimRegex,
            GroupAttributeField=GroupAttributeField,
            Issuer=Issuer,
            SecretManagerArn=SecretManagerArn,
            URL=URL,
            UserNameAttributeField=UserNameAttributeField,
            **kwargs
        )
        super(JwtTokenTypeConfiguration, self).__init__(**processed_kwargs)


class UserTokenConfiguration(troposphere.kendra.UserTokenConfiguration, Mixin):
    def __init__(self,
                 title=None,
                 JsonTokenTypeConfiguration=NOTHING, # type: _JsonTokenTypeConfiguration
                 JwtTokenTypeConfiguration=NOTHING, # type: _JwtTokenTypeConfiguration
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            JsonTokenTypeConfiguration=JsonTokenTypeConfiguration,
            JwtTokenTypeConfiguration=JwtTokenTypeConfiguration,
            **kwargs
        )
        super(UserTokenConfiguration, self).__init__(**processed_kwargs)


class Index(troposphere.kendra.Index, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Edition=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 CapacityUnits=NOTHING, # type: _CapacityUnitsConfiguration
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 DocumentMetadataConfigurations=NOTHING, # type: List[_DocumentMetadataConfiguration]
                 ServerSideEncryptionConfiguration=NOTHING, # type: _ServerSideEncryptionConfiguration
                 Tags=NOTHING, # type: _Tags
                 UserContextPolicy=NOTHING, # type: Union[str, AWSHelperFn]
                 UserTokenConfigurations=NOTHING, # type: List[_UserTokenConfiguration]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Edition=Edition,
            Name=Name,
            RoleArn=RoleArn,
            CapacityUnits=CapacityUnits,
            Description=Description,
            DocumentMetadataConfigurations=DocumentMetadataConfigurations,
            ServerSideEncryptionConfiguration=ServerSideEncryptionConfiguration,
            Tags=Tags,
            UserContextPolicy=UserContextPolicy,
            UserTokenConfigurations=UserTokenConfigurations,
            **kwargs
        )
        super(Index, self).__init__(**processed_kwargs)
