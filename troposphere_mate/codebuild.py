# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.codebuild

from troposphere.codebuild import (
    Artifacts as _Artifacts,
    BatchRestrictions as _BatchRestrictions,
    BuildStatusConfig as _BuildStatusConfig,
    CloudWatchLogs as _CloudWatchLogs,
    Environment as _Environment,
    GitSubmodulesConfig as _GitSubmodulesConfig,
    LogsConfig as _LogsConfig,
    ProjectBuildBatchConfig as _ProjectBuildBatchConfig,
    ProjectCache as _ProjectCache,
    ProjectFileSystemLocation as _ProjectFileSystemLocation,
    ProjectSourceVersion as _ProjectSourceVersion,
    ProjectTriggers as _ProjectTriggers,
    RegistryCredential as _RegistryCredential,
    ReportExportConfig as _ReportExportConfig,
    S3Logs as _S3Logs,
    S3ReportExportConfig as _S3ReportExportConfig,
    Source as _Source,
    SourceAuth as _SourceAuth,
    Tags as _Tags,
    VpcConfig as _VpcConfig,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class SourceAuth(troposphere.codebuild.SourceAuth, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Resource=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Resource=Resource,
            **kwargs
        )
        super(SourceAuth, self).__init__(**processed_kwargs)


class Artifacts(troposphere.codebuild.Artifacts, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 ArtifactIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 EncryptionDisabled=NOTHING, # type: bool
                 Location=NOTHING, # type: Union[str, AWSHelperFn]
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 NamespaceType=NOTHING, # type: Union[str, AWSHelperFn]
                 OverrideArtifactName=NOTHING, # type: bool
                 Packaging=NOTHING, # type: Union[str, AWSHelperFn]
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            ArtifactIdentifier=ArtifactIdentifier,
            EncryptionDisabled=EncryptionDisabled,
            Location=Location,
            Name=Name,
            NamespaceType=NamespaceType,
            OverrideArtifactName=OverrideArtifactName,
            Packaging=Packaging,
            Path=Path,
            **kwargs
        )
        super(Artifacts, self).__init__(**processed_kwargs)


class EnvironmentVariable(troposphere.codebuild.EnvironmentVariable, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            Type=Type,
            **kwargs
        )
        super(EnvironmentVariable, self).__init__(**processed_kwargs)


class RegistryCredential(troposphere.codebuild.RegistryCredential, Mixin):
    def __init__(self,
                 title=None,
                 Credential=REQUIRED, # type: Union[str, AWSHelperFn]
                 CredentialProvider=REQUIRED, # type: Any
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Credential=Credential,
            CredentialProvider=CredentialProvider,
            **kwargs
        )
        super(RegistryCredential, self).__init__(**processed_kwargs)


class Environment(troposphere.codebuild.Environment, Mixin):
    def __init__(self,
                 title=None,
                 ComputeType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Image=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Certificate=NOTHING, # type: Union[str, AWSHelperFn]
                 ImagePullCredentialsType=NOTHING, # type: Any
                 PrivilegedMode=NOTHING, # type: bool
                 RegistryCredential=NOTHING, # type: _RegistryCredential
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComputeType=ComputeType,
            Image=Image,
            Type=Type,
            Certificate=Certificate,
            ImagePullCredentialsType=ImagePullCredentialsType,
            PrivilegedMode=PrivilegedMode,
            RegistryCredential=RegistryCredential,
            **kwargs
        )
        super(Environment, self).__init__(**processed_kwargs)


class BatchRestrictions(troposphere.codebuild.BatchRestrictions, Mixin):
    def __init__(self,
                 title=None,
                 ComputeTypesAllowed=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 MaximumBuildsAllowed=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ComputeTypesAllowed=ComputeTypesAllowed,
            MaximumBuildsAllowed=MaximumBuildsAllowed,
            **kwargs
        )
        super(BatchRestrictions, self).__init__(**processed_kwargs)


class ProjectBuildBatchConfig(troposphere.codebuild.ProjectBuildBatchConfig, Mixin):
    def __init__(self,
                 title=None,
                 CombineArtifacts=NOTHING, # type: bool
                 Restrictions=NOTHING, # type: _BatchRestrictions
                 ServiceRole=NOTHING, # type: Union[str, AWSHelperFn]
                 TimeoutInMins=NOTHING, # type: int
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CombineArtifacts=CombineArtifacts,
            Restrictions=Restrictions,
            ServiceRole=ServiceRole,
            TimeoutInMins=TimeoutInMins,
            **kwargs
        )
        super(ProjectBuildBatchConfig, self).__init__(**processed_kwargs)


class ProjectCache(troposphere.codebuild.ProjectCache, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Location=NOTHING, # type: Union[str, AWSHelperFn]
                 Modes=NOTHING, # type: List[Union[str, AWSHelperFn]]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Location=Location,
            Modes=Modes,
            **kwargs
        )
        super(ProjectCache, self).__init__(**processed_kwargs)


class BuildStatusConfig(troposphere.codebuild.BuildStatusConfig, Mixin):
    def __init__(self,
                 title=None,
                 Context=NOTHING, # type: Union[str, AWSHelperFn]
                 TargetUrl=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Context=Context,
            TargetUrl=TargetUrl,
            **kwargs
        )
        super(BuildStatusConfig, self).__init__(**processed_kwargs)


class GitSubmodulesConfig(troposphere.codebuild.GitSubmodulesConfig, Mixin):
    def __init__(self,
                 title=None,
                 FetchSubmodules=REQUIRED, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            FetchSubmodules=FetchSubmodules,
            **kwargs
        )
        super(GitSubmodulesConfig, self).__init__(**processed_kwargs)


class Source(troposphere.codebuild.Source, Mixin):
    def __init__(self,
                 title=None,
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 Auth=NOTHING, # type: _SourceAuth
                 BuildSpec=NOTHING, # type: Union[str, AWSHelperFn]
                 BuildStatusConfig=NOTHING, # type: _BuildStatusConfig
                 GitCloneDepth=NOTHING, # type: int
                 GitSubmodulesConfig=NOTHING, # type: _GitSubmodulesConfig
                 InsecureSsl=NOTHING, # type: bool
                 Location=NOTHING, # type: Union[str, AWSHelperFn]
                 ReportBuildStatus=NOTHING, # type: bool
                 SourceIdentifier=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Type=Type,
            Auth=Auth,
            BuildSpec=BuildSpec,
            BuildStatusConfig=BuildStatusConfig,
            GitCloneDepth=GitCloneDepth,
            GitSubmodulesConfig=GitSubmodulesConfig,
            InsecureSsl=InsecureSsl,
            Location=Location,
            ReportBuildStatus=ReportBuildStatus,
            SourceIdentifier=SourceIdentifier,
            **kwargs
        )
        super(Source, self).__init__(**processed_kwargs)


class VpcConfig(troposphere.codebuild.VpcConfig, Mixin):
    def __init__(self,
                 title=None,
                 SecurityGroupIds=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 Subnets=REQUIRED, # type: List[Union[str, AWSHelperFn]]
                 VpcId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SecurityGroupIds=SecurityGroupIds,
            Subnets=Subnets,
            VpcId=VpcId,
            **kwargs
        )
        super(VpcConfig, self).__init__(**processed_kwargs)


class WebhookFilter(troposphere.codebuild.WebhookFilter, Mixin):
    def __init__(self,
                 title=None,
                 Pattern=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Any
                 ExcludeMatchedPattern=NOTHING, # type: bool
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Pattern=Pattern,
            Type=Type,
            ExcludeMatchedPattern=ExcludeMatchedPattern,
            **kwargs
        )
        super(WebhookFilter, self).__init__(**processed_kwargs)


class ProjectTriggers(troposphere.codebuild.ProjectTriggers, Mixin):
    def __init__(self,
                 title=None,
                 Webhook=NOTHING, # type: bool
                 FilterGroups=NOTHING, # type: list
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Webhook=Webhook,
            FilterGroups=FilterGroups,
            **kwargs
        )
        super(ProjectTriggers, self).__init__(**processed_kwargs)


class CloudWatchLogs(troposphere.codebuild.CloudWatchLogs, Mixin):
    def __init__(self,
                 title=None,
                 Status=REQUIRED, # type: Any
                 GroupName=NOTHING, # type: Union[str, AWSHelperFn]
                 StreamName=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            GroupName=GroupName,
            StreamName=StreamName,
            **kwargs
        )
        super(CloudWatchLogs, self).__init__(**processed_kwargs)


class S3Logs(troposphere.codebuild.S3Logs, Mixin):
    def __init__(self,
                 title=None,
                 Status=REQUIRED, # type: Any
                 EncryptionDisabled=NOTHING, # type: bool
                 Location=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Status=Status,
            EncryptionDisabled=EncryptionDisabled,
            Location=Location,
            **kwargs
        )
        super(S3Logs, self).__init__(**processed_kwargs)


class LogsConfig(troposphere.codebuild.LogsConfig, Mixin):
    def __init__(self,
                 title=None,
                 CloudWatchLogs=NOTHING, # type: _CloudWatchLogs
                 S3Logs=NOTHING, # type: _S3Logs
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CloudWatchLogs=CloudWatchLogs,
            S3Logs=S3Logs,
            **kwargs
        )
        super(LogsConfig, self).__init__(**processed_kwargs)


class ProjectSourceVersion(troposphere.codebuild.ProjectSourceVersion, Mixin):
    def __init__(self,
                 title=None,
                 SourceIdentifier=REQUIRED, # type: Union[str, AWSHelperFn]
                 SourceVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            SourceIdentifier=SourceIdentifier,
            SourceVersion=SourceVersion,
            **kwargs
        )
        super(ProjectSourceVersion, self).__init__(**processed_kwargs)


class ProjectFileSystemLocation(troposphere.codebuild.ProjectFileSystemLocation, Mixin):
    def __init__(self,
                 title=None,
                 Identifier=REQUIRED, # type: Union[str, AWSHelperFn]
                 Location=REQUIRED, # type: Union[str, AWSHelperFn]
                 MountPoint=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Any
                 MountOptions=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Identifier=Identifier,
            Location=Location,
            MountPoint=MountPoint,
            Type=Type,
            MountOptions=MountOptions,
            **kwargs
        )
        super(ProjectFileSystemLocation, self).__init__(**processed_kwargs)


class Project(troposphere.codebuild.Project, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 Artifacts=REQUIRED, # type: _Artifacts
                 Environment=REQUIRED, # type: _Environment
                 ServiceRole=REQUIRED, # type: Union[str, AWSHelperFn]
                 Source=REQUIRED, # type: _Source
                 BadgeEnabled=NOTHING, # type: bool
                 BuildBatchConfig=NOTHING, # type: _ProjectBuildBatchConfig
                 Cache=NOTHING, # type: _ProjectCache
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 EncryptionKey=NOTHING, # type: Union[str, AWSHelperFn]
                 FileSystemLocations=NOTHING, # type: List[_ProjectFileSystemLocation]
                 LogsConfig=NOTHING, # type: _LogsConfig
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 QueuedTimeoutInMinutes=NOTHING, # type: int
                 SecondaryArtifacts=NOTHING, # type: List[_Artifacts]
                 SecondarySourceVersions=NOTHING, # type: List[_ProjectSourceVersion]
                 SecondarySources=NOTHING, # type: List[_Source]
                 SourceVersion=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 TimeoutInMinutes=NOTHING, # type: int
                 Triggers=NOTHING, # type: _ProjectTriggers
                 VpcConfig=NOTHING, # type: _VpcConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            Artifacts=Artifacts,
            Environment=Environment,
            ServiceRole=ServiceRole,
            Source=Source,
            BadgeEnabled=BadgeEnabled,
            BuildBatchConfig=BuildBatchConfig,
            Cache=Cache,
            Description=Description,
            EncryptionKey=EncryptionKey,
            FileSystemLocations=FileSystemLocations,
            LogsConfig=LogsConfig,
            Name=Name,
            QueuedTimeoutInMinutes=QueuedTimeoutInMinutes,
            SecondaryArtifacts=SecondaryArtifacts,
            SecondarySourceVersions=SecondarySourceVersions,
            SecondarySources=SecondarySources,
            SourceVersion=SourceVersion,
            Tags=Tags,
            TimeoutInMinutes=TimeoutInMinutes,
            Triggers=Triggers,
            VpcConfig=VpcConfig,
            **kwargs
        )
        super(Project, self).__init__(**processed_kwargs)


class S3ReportExportConfig(troposphere.codebuild.S3ReportExportConfig, Mixin):
    def __init__(self,
                 title=None,
                 Bucket=REQUIRED, # type: Union[str, AWSHelperFn]
                 EncryptionDisabled=NOTHING, # type: bool
                 EncryptionKey=NOTHING, # type: Union[str, AWSHelperFn]
                 Packaging=NOTHING, # type: Union[str, AWSHelperFn]
                 Path=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Bucket=Bucket,
            EncryptionDisabled=EncryptionDisabled,
            EncryptionKey=EncryptionKey,
            Packaging=Packaging,
            Path=Path,
            **kwargs
        )
        super(S3ReportExportConfig, self).__init__(**processed_kwargs)


class ReportExportConfig(troposphere.codebuild.ReportExportConfig, Mixin):
    def __init__(self,
                 title=None,
                 ExportConfigType=REQUIRED, # type: Union[str, AWSHelperFn]
                 S3Destination=NOTHING, # type: _S3ReportExportConfig
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ExportConfigType=ExportConfigType,
            S3Destination=S3Destination,
            **kwargs
        )
        super(ReportExportConfig, self).__init__(**processed_kwargs)


class ReportGroup(troposphere.codebuild.ReportGroup, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 ExportConfig=REQUIRED, # type: _ReportExportConfig
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 DeleteReports=NOTHING, # type: bool
                 Name=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            ExportConfig=ExportConfig,
            Type=Type,
            DeleteReports=DeleteReports,
            Name=Name,
            Tags=Tags,
            **kwargs
        )
        super(ReportGroup, self).__init__(**processed_kwargs)


class SourceCredential(troposphere.codebuild.SourceCredential, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AuthType=REQUIRED, # type: Union[str, AWSHelperFn]
                 ServerType=REQUIRED, # type: Union[str, AWSHelperFn]
                 Token=REQUIRED, # type: Union[str, AWSHelperFn]
                 Username=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AuthType=AuthType,
            ServerType=ServerType,
            Token=Token,
            Username=Username,
            **kwargs
        )
        super(SourceCredential, self).__init__(**processed_kwargs)
