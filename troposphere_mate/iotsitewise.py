# -*- coding: utf-8 -*-

"""
This code is auto generated from troposphere_mate.code_generator.__init__.py scripts.
"""

import sys
if sys.version_info.major >= 3 and sys.version_info.minor >= 5:  # pragma: no cover
    from typing import Union, List, Any

import troposphere.iotsitewise

from troposphere.iotsitewise import (
    AccessPolicyIdentity as _AccessPolicyIdentity,
    AccessPolicyResource as _AccessPolicyResource,
    AssetHierarchy as _AssetHierarchy,
    AssetModelCompositeModel as _AssetModelCompositeModel,
    AssetModelHierarchy as _AssetModelHierarchy,
    AssetModelProperty as _AssetModelProperty,
    AssetProperty as _AssetProperty,
    Attribute as _Attribute,
    ExpressionVariable as _ExpressionVariable,
    GatewayCapabilitySummary as _GatewayCapabilitySummary,
    GatewayPlatform as _GatewayPlatform,
    Greengrass as _Greengrass,
    IamRole as _IamRole,
    IamUser as _IamUser,
    Metric as _Metric,
    MetricWindow as _MetricWindow,
    PortalProperty as _PortalProperty,
    Project as _Project,
    PropertyType as _PropertyType,
    Tags as _Tags,
    Transform as _Transform,
    TumblingWindow as _TumblingWindow,
    User as _User,
    VariableValue as _VariableValue,
)


from troposphere import Template, AWSHelperFn
from troposphere_mate.core.mate import preprocess_init_kwargs, Mixin
from troposphere_mate.core.sentiel import REQUIRED, NOTHING



class IamRole(troposphere.iotsitewise.IamRole, Mixin):
    def __init__(self,
                 title=None,
                 arn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            arn=arn,
            **kwargs
        )
        super(IamRole, self).__init__(**processed_kwargs)


class IamUser(troposphere.iotsitewise.IamUser, Mixin):
    def __init__(self,
                 title=None,
                 arn=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            arn=arn,
            **kwargs
        )
        super(IamUser, self).__init__(**processed_kwargs)


class User(troposphere.iotsitewise.User, Mixin):
    def __init__(self,
                 title=None,
                 id=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            id=id,
            **kwargs
        )
        super(User, self).__init__(**processed_kwargs)


class AccessPolicyIdentity(troposphere.iotsitewise.AccessPolicyIdentity, Mixin):
    def __init__(self,
                 title=None,
                 IamRole=NOTHING, # type: _IamRole
                 IamUser=NOTHING, # type: _IamUser
                 User=NOTHING, # type: _User
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            IamRole=IamRole,
            IamUser=IamUser,
            User=User,
            **kwargs
        )
        super(AccessPolicyIdentity, self).__init__(**processed_kwargs)


class PortalProperty(troposphere.iotsitewise.PortalProperty, Mixin):
    def __init__(self,
                 title=None,
                 id=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            id=id,
            **kwargs
        )
        super(PortalProperty, self).__init__(**processed_kwargs)


class Project(troposphere.iotsitewise.Project, Mixin):
    def __init__(self,
                 title=None,
                 id=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            id=id,
            **kwargs
        )
        super(Project, self).__init__(**processed_kwargs)


class AccessPolicyResource(troposphere.iotsitewise.AccessPolicyResource, Mixin):
    def __init__(self,
                 title=None,
                 Portal=NOTHING, # type: _PortalProperty
                 Project=NOTHING, # type: _Project
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Portal=Portal,
            Project=Project,
            **kwargs
        )
        super(AccessPolicyResource, self).__init__(**processed_kwargs)


class AccessPolicy(troposphere.iotsitewise.AccessPolicy, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AccessPolicyIdentity=REQUIRED, # type: _AccessPolicyIdentity
                 AccessPolicyPermission=REQUIRED, # type: Union[str, AWSHelperFn]
                 AccessPolicyResource=REQUIRED, # type: _AccessPolicyResource
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AccessPolicyIdentity=AccessPolicyIdentity,
            AccessPolicyPermission=AccessPolicyPermission,
            AccessPolicyResource=AccessPolicyResource,
            **kwargs
        )
        super(AccessPolicy, self).__init__(**processed_kwargs)


class AssetHierarchy(troposphere.iotsitewise.AssetHierarchy, Mixin):
    def __init__(self,
                 title=None,
                 ChildAssetId=REQUIRED, # type: Union[str, AWSHelperFn]
                 LogicalId=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ChildAssetId=ChildAssetId,
            LogicalId=LogicalId,
            **kwargs
        )
        super(AssetHierarchy, self).__init__(**processed_kwargs)


class AssetProperty(troposphere.iotsitewise.AssetProperty, Mixin):
    def __init__(self,
                 title=None,
                 LogicalId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Alias=NOTHING, # type: Union[str, AWSHelperFn]
                 NotificationState=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            LogicalId=LogicalId,
            Alias=Alias,
            NotificationState=NotificationState,
            **kwargs
        )
        super(AssetProperty, self).__init__(**processed_kwargs)


class Asset(troposphere.iotsitewise.Asset, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AssetModelId=REQUIRED, # type: Union[str, AWSHelperFn]
                 AssetName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AssetHierarchies=NOTHING, # type: List[_AssetHierarchy]
                 AssetProperties=NOTHING, # type: List[_AssetProperty]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AssetModelId=AssetModelId,
            AssetName=AssetName,
            AssetHierarchies=AssetHierarchies,
            AssetProperties=AssetProperties,
            Tags=Tags,
            **kwargs
        )
        super(Asset, self).__init__(**processed_kwargs)


class Attribute(troposphere.iotsitewise.Attribute, Mixin):
    def __init__(self,
                 title=None,
                 DefaultValue=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DefaultValue=DefaultValue,
            **kwargs
        )
        super(Attribute, self).__init__(**processed_kwargs)


class VariableValue(troposphere.iotsitewise.VariableValue, Mixin):
    def __init__(self,
                 title=None,
                 PropertyLogicalId=REQUIRED, # type: Union[str, AWSHelperFn]
                 HierarchyLogicalId=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            PropertyLogicalId=PropertyLogicalId,
            HierarchyLogicalId=HierarchyLogicalId,
            **kwargs
        )
        super(VariableValue, self).__init__(**processed_kwargs)


class ExpressionVariable(troposphere.iotsitewise.ExpressionVariable, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Value=REQUIRED, # type: _VariableValue
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Value=Value,
            **kwargs
        )
        super(ExpressionVariable, self).__init__(**processed_kwargs)


class TumblingWindow(troposphere.iotsitewise.TumblingWindow, Mixin):
    def __init__(self,
                 title=None,
                 Interval=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Interval=Interval,
            **kwargs
        )
        super(TumblingWindow, self).__init__(**processed_kwargs)


class MetricWindow(troposphere.iotsitewise.MetricWindow, Mixin):
    def __init__(self,
                 title=None,
                 Tumbling=NOTHING, # type: _TumblingWindow
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Tumbling=Tumbling,
            **kwargs
        )
        super(MetricWindow, self).__init__(**processed_kwargs)


class Metric(troposphere.iotsitewise.Metric, Mixin):
    def __init__(self,
                 title=None,
                 Expression=REQUIRED, # type: Union[str, AWSHelperFn]
                 Variables=REQUIRED, # type: List[_ExpressionVariable]
                 Window=REQUIRED, # type: _MetricWindow
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Expression=Expression,
            Variables=Variables,
            Window=Window,
            **kwargs
        )
        super(Metric, self).__init__(**processed_kwargs)


class Transform(troposphere.iotsitewise.Transform, Mixin):
    def __init__(self,
                 title=None,
                 Expression=REQUIRED, # type: Union[str, AWSHelperFn]
                 Variables=REQUIRED, # type: List[_ExpressionVariable]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Expression=Expression,
            Variables=Variables,
            **kwargs
        )
        super(Transform, self).__init__(**processed_kwargs)


class PropertyType(troposphere.iotsitewise.PropertyType, Mixin):
    def __init__(self,
                 title=None,
                 TypeName=REQUIRED, # type: Union[str, AWSHelperFn]
                 Attribute=NOTHING, # type: _Attribute
                 Metric=NOTHING, # type: _Metric
                 Transform=NOTHING, # type: _Transform
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            TypeName=TypeName,
            Attribute=Attribute,
            Metric=Metric,
            Transform=Transform,
            **kwargs
        )
        super(PropertyType, self).__init__(**processed_kwargs)


class AssetModelProperty(troposphere.iotsitewise.AssetModelProperty, Mixin):
    def __init__(self,
                 title=None,
                 DataType=REQUIRED, # type: Union[str, AWSHelperFn]
                 LogicalId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: _PropertyType
                 DataTypeSpec=NOTHING, # type: Union[str, AWSHelperFn]
                 Unit=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            DataType=DataType,
            LogicalId=LogicalId,
            Name=Name,
            Type=Type,
            DataTypeSpec=DataTypeSpec,
            Unit=Unit,
            **kwargs
        )
        super(AssetModelProperty, self).__init__(**processed_kwargs)


class AssetModelCompositeModel(troposphere.iotsitewise.AssetModelCompositeModel, Mixin):
    def __init__(self,
                 title=None,
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 Type=REQUIRED, # type: Union[str, AWSHelperFn]
                 CompositeModelProperties=NOTHING, # type: List[_AssetModelProperty]
                 Description=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Name=Name,
            Type=Type,
            CompositeModelProperties=CompositeModelProperties,
            Description=Description,
            **kwargs
        )
        super(AssetModelCompositeModel, self).__init__(**processed_kwargs)


class AssetModelHierarchy(troposphere.iotsitewise.AssetModelHierarchy, Mixin):
    def __init__(self,
                 title=None,
                 ChildAssetModelId=REQUIRED, # type: Union[str, AWSHelperFn]
                 LogicalId=REQUIRED, # type: Union[str, AWSHelperFn]
                 Name=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            ChildAssetModelId=ChildAssetModelId,
            LogicalId=LogicalId,
            Name=Name,
            **kwargs
        )
        super(AssetModelHierarchy, self).__init__(**processed_kwargs)


class AssetModel(troposphere.iotsitewise.AssetModel, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 AssetModelName=REQUIRED, # type: Union[str, AWSHelperFn]
                 AssetModelCompositeModels=NOTHING, # type: List[_AssetModelCompositeModel]
                 AssetModelDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 AssetModelHierarchies=NOTHING, # type: List[_AssetModelHierarchy]
                 AssetModelProperties=NOTHING, # type: List[_AssetModelProperty]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            AssetModelName=AssetModelName,
            AssetModelCompositeModels=AssetModelCompositeModels,
            AssetModelDescription=AssetModelDescription,
            AssetModelHierarchies=AssetModelHierarchies,
            AssetModelProperties=AssetModelProperties,
            Tags=Tags,
            **kwargs
        )
        super(AssetModel, self).__init__(**processed_kwargs)


class Dashboard(troposphere.iotsitewise.Dashboard, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 DashboardDefinition=REQUIRED, # type: Union[str, AWSHelperFn]
                 DashboardDescription=REQUIRED, # type: Union[str, AWSHelperFn]
                 DashboardName=REQUIRED, # type: Union[str, AWSHelperFn]
                 ProjectId=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            DashboardDefinition=DashboardDefinition,
            DashboardDescription=DashboardDescription,
            DashboardName=DashboardName,
            ProjectId=ProjectId,
            Tags=Tags,
            **kwargs
        )
        super(Dashboard, self).__init__(**processed_kwargs)


class GatewayCapabilitySummary(troposphere.iotsitewise.GatewayCapabilitySummary, Mixin):
    def __init__(self,
                 title=None,
                 CapabilityNamespace=REQUIRED, # type: Union[str, AWSHelperFn]
                 CapabilityConfiguration=NOTHING, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            CapabilityNamespace=CapabilityNamespace,
            CapabilityConfiguration=CapabilityConfiguration,
            **kwargs
        )
        super(GatewayCapabilitySummary, self).__init__(**processed_kwargs)


class Greengrass(troposphere.iotsitewise.Greengrass, Mixin):
    def __init__(self,
                 title=None,
                 GroupArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            GroupArn=GroupArn,
            **kwargs
        )
        super(Greengrass, self).__init__(**processed_kwargs)


class GatewayPlatform(troposphere.iotsitewise.GatewayPlatform, Mixin):
    def __init__(self,
                 title=None,
                 Greengrass=REQUIRED, # type: _Greengrass
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            Greengrass=Greengrass,
            **kwargs
        )
        super(GatewayPlatform, self).__init__(**processed_kwargs)


class Gateway(troposphere.iotsitewise.Gateway, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 GatewayName=REQUIRED, # type: Union[str, AWSHelperFn]
                 GatewayPlatform=REQUIRED, # type: _GatewayPlatform
                 GatewayCapabilitySummaries=NOTHING, # type: List[_GatewayCapabilitySummary]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            GatewayName=GatewayName,
            GatewayPlatform=GatewayPlatform,
            GatewayCapabilitySummaries=GatewayCapabilitySummaries,
            Tags=Tags,
            **kwargs
        )
        super(Gateway, self).__init__(**processed_kwargs)


class Portal(troposphere.iotsitewise.Portal, Mixin):
    def __init__(self,
                 title, # type: str
                 template=None, # type: Template
                 validation=True, # type: bool
                 PortalContactEmail=REQUIRED, # type: Union[str, AWSHelperFn]
                 PortalName=REQUIRED, # type: Union[str, AWSHelperFn]
                 RoleArn=REQUIRED, # type: Union[str, AWSHelperFn]
                 PortalAuthMode=NOTHING, # type: Union[str, AWSHelperFn]
                 PortalDescription=NOTHING, # type: Union[str, AWSHelperFn]
                 Tags=NOTHING, # type: _Tags
                 **kwargs):
        processed_kwargs = preprocess_init_kwargs(
            title=title,
            template=template,
            validation=validation,
            PortalContactEmail=PortalContactEmail,
            PortalName=PortalName,
            RoleArn=RoleArn,
            PortalAuthMode=PortalAuthMode,
            PortalDescription=PortalDescription,
            Tags=Tags,
            **kwargs
        )
        super(Portal, self).__init__(**processed_kwargs)
