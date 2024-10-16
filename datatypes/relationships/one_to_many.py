from datatypes.relationships.interfaces.abstract_relationship import AbstractRelationship
from enumerations import RelationshipName
from subsystem.hvac_components.interfaces.abstract_hvac_component import AbstractHVACComponent
from subsystem.hvac_components.interfaces.abstract_duct_connected_component import AbstractDuctConnectedComponent
from typing import Union
from typing import List


class OneToMany(AbstractRelationship):

    def __init__(self, name: RelationshipName, hvac_component: Union[List[AbstractHVACComponent],
    List[AbstractDuctConnectedComponent]]):
        super().__init__(name)
        self.component = hvac_component