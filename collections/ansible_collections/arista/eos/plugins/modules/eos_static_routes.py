#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for eos_static_routes
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: eos_static_routes
short_description: Static routes resource module
description: This module configures and manages the attributes of static routes on
  Arista EOS platforms.
version_added: 1.0.0
author: Gomathi Selvi Srinivasan (@GomathiselviS)
notes:
- Tested against Arista EOS 4.20.10M
- This module works with connection C(network_cli). See the L(EOS Platform Options,../network/user_guide/platform_eos.html).
options:
  config:
    description:
    - A list of configurations for static routes.
    type: list
    elements: dict
    suboptions:
      vrf:
        description:
        - The VRF to which the static route(s) belong.
        type: str
      address_families:
        description: A dictionary specifying the address family to which the static
          route(s) belong.
        type: list
        elements: dict
        suboptions:
          afi:
            description:
            - Specifies the top level address family indicator.
            type: str
            choices:
            - ipv4
            - ipv6
            required: true
          routes:
            description: A dictionary that specifies the static route configurations.
            elements: dict
            type: list
            suboptions:
              dest:
                description:
                - Destination IPv4 subnet (CIDR or address-mask notation).
                - The address format is <v4/v6 address>/<mask> or <v4/v6 address>
                  <mask>.
                - The mask is number in range 0-32 for IPv4 and in range 0-128 for
                  IPv6.
                type: str
                required: true
              next_hops:
                description:
                - Details of route to be taken.
                type: list
                elements: dict
                suboptions:
                  forward_router_address:
                    description:
                    - Forwarding router's address on destination interface.
                    type: str
                  interface:
                    description:
                    - Outgoing interface to take. For anything except 'null0', then
                      next hop IP address should also be configured.
                    - IP address of the next hop router or
                    - null0 Null0 interface or
                    - ethernet e_num Ethernet interface or
                    - loopback l_num Loopback interface or
                    - management m_num Management interface or
                    - port-channel p_num
                    - vlan v_num
                    - vxlan vx_num
                    - Nexthop-Group  Specify nexthop group name
                    - Tunnel  Tunnel interface
                    - vtep  Configure VXLAN Tunnel End Points
                    type: str
                  nexthop_grp:
                    description:
                    - Nexthop group
                    type: str
                  admin_distance:
                    description:
                    - Preference or administrative distance of route (range 1-255).
                    type: int
                  description:
                    description:
                    - Name of the static route.
                    type: str
                  tag:
                    description:
                    - Route tag value (ranges from 0 to 4294967295).
                    type: int
                  track:
                    description:
                    - Track value (range 1 - 512). Track must already be configured
                      on the device before adding the route.
                    type: str
                  mpls_label:
                    description:
                    - MPLS label
                    type: int
                  vrf:
                    description:
                    - VRF of the destination.
                    type: str
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the EOS device by
      executing the command B(show running-config | grep routes).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state the configuration should be left in.
    type: str
    choices:
    - deleted
    - merged
    - overridden
    - replaced
    - gathered
    - rendered
    - parsed
    default: merged

"""
EXAMPLES = """
# Using deleted

# Before State:
# ------------

# veos(config)#show running-config | grep route
# ip route vrf testvrf 22.65.1.0/24 Null0 90 name testroute
# ipv6 route 5222:5::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Ethernet1 55
# ipv6 route vrf testvrf 2222:6::/64 Null0 90 name testroute1
# veos(config)#

- name: Delete afi
  arista.eos.eos_static_routes:
    config:
    - vrf: testvrf
      address_families:
      - afi: ipv4
    state: deleted

#    "after": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5222:5::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2222:6::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                },
#                                {
#                                    "admin_distance": 55,
#                                    "interface": "Ethernet1"
#                                },
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute1",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ],
#    "before": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5222:5::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "22.65.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2222:6::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                },
#                                {
#                                    "admin_distance": 55,
#                                    "interface": "Ethernet1"
#                                },
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute1",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ],
#    "changed": true,
#    "commands": [
#        "no ip route vrf testvrf 22.65.1.0/24 Null0 90 name testroute"
#    ],

# After State
# ___________

# veos(config)#show running-config | grep route
# ipv6 route 5222:5::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Ethernet1 55
# ipv6 route vrf testvrf 2222:6::/64 Null0 90 name testroute1

#
# Using merged

# Before : [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "165.10.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 100,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "172.17.252.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgroup"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5001::/64",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 50,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "130.1.122.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1",
#                                    "tag": 50
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ]
#
# Before State
# -------------
# veos(config)#show running-config | grep "route"
# ip route 165.10.1.0/24 Ethernet1 100
# ip route 172.17.252.0/24 Nexthop-Group testgroup
# ip route vrf testvrf 130.1.122.0/24 Ethernet1 tag 50
# ipv6 route 5001::/64 Ethernet1 50
# veos(config)#

- name: Merge new static route configuration
  arista.eos.eos_static_routes:
    config:
    - vrf: testvrf
      address_families:
      - afi: ipv6
        routes:
        - dest: 2211::0/64
          next_hop:
          - forward_router_address: 100:1::2
            interface: Ethernet1
    state: merged

# After State
# -----------

#After [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "165.10.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 100,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "172.17.252.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgroup"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5001::/64",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 50,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "130.1.122.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1",
#                                    "tag": 50
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2211::0/64",
#                            "next_hops": [
#                                {
#                                    "aforward_router_address": 100:1::2
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }

#            ],
#            "vrf": "testvrf"
#        }
#    ]
#
# veos(config)#show running-config | grep "route"
# ip route 165.10.1.0/24 Ethernet1 100
# ip route 172.17.252.0/24 Nexthop-Group testgroup
# ip route vrf testvrf 130.1.122.0/24 Ethernet1 tag 50
# ipv6 route 2211::/64 Ethernet1 100:1::2
# ipv6 route 5001::/64 Ethernet1 50
# veos(config)#


# Using overridden


# Before State
# -------------

#    "before": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "165.10.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 100,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "172.17.252.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgroup"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5001::/64",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 50,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "130.1.122.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1",
#                                    "tag": 50
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ]
# veos(config)#show running-config | grep "route"
# ip route 165.10.1.0/24 Ethernet1 100
# ip route 172.17.252.0/24 Nexthop-Group testgroup
# ip route vrf testvrf 130.1.122.0/24 Ethernet1 tag 50
# ipv6 route 5001::/64 Ethernet1 50
# veos(config)#

- name: Overridden static route configuration
  arista.eos.eos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 10.2.2.0/24
          next_hop:
          - interface: Ethernet1
    state: replaced

# After State
# -----------

# "after": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "10.2.2.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        }
#    ]
# veos(config)#show running-config | grep "route"
# ip route 10.2.2.0/24 Ethernet1
# veos(config)#


# Using replaced

# Before State
# -------------

# ip route 10.2.2.0/24 Ethernet1
# ip route 10.2.2.0/24 64.1.1.1 label 17 33
# ip route 33.33.33.0/24 Nexthop-Group testgrp
# ip route vrf testvrf 22.65.1.0/24 Null0 90 name testroute
# ipv6 route 5222:5::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Ethernet1 55
# ipv6 route vrf testvrf 2222:6::/64 Null0 90 name testroute1

# [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "10.2.2.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1"
#                                },
#                                {
#                                    "admin_distance": 33,
#                                    "interface": "64.1.1.1",
#                                    "mpls_label": 17
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "33.33.33.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgrp"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5222:5::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "22.65.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2222:6::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                },
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute1",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ]

- name: Replace nexthop
  arista.eos.eos_static_routes:
    config:
    - vrf: testvrf
      address_families:
      - afi: ipv6
        routes:
        - dest: 2222:6::/64
          next_hops:
          - admin_distance: 55
            interface: Ethernet1
    state: replaced

# After State
# -----------

# veos(config)#show running-config | grep route
# ip route 10.2.2.0/24 Ethernet1
# ip route 10.2.2.0/24 64.1.1.1 label 17 33
# ip route 33.33.33.0/24 Nexthop-Group testgrp
# ip route vrf testvrf 22.65.1.0/24 Null0 90 name testroute
# ipv6 route 5222:5::/64 Management1 4312:100::1
# ipv6 route vrf testvrf 2222:6::/64 Ethernet1 55

# "after": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "10.2.2.0/24",
#                            "next_hops": [
#                                {
#                                    "interface": "Ethernet1"
#                                },
#                                {
#                                    "admin_distance": 33,
#                                    "interface": "64.1.1.1",
#                                    "mpls_label": 17
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "33.33.33.0/24",
#                            "next_hops": [
#                                {
#                                    "nexthop_grp": "testgrp"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "5222:5::/64",
#                            "next_hops": [
#                                {
#                                    "forward_router_address": "4312:100::1",
#                                    "interface": "Management1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "22.65.1.0/24",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 90,
#                                    "description": "testroute",
#                                    "interface": "Null0"
#                                }
#                            ]
#                        }
#                    ]
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2222:6::/64",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 55,
#                                    "interface": "Ethernet1"
#                                }
#                            ]
#                        }
#                    ]
#                }
#            ],
#            "vrf": "testvrf"
#        }
#    ]

# Before State
# -------------
# veos(config)#show running-config | grep "route"
# ip route 165.10.1.0/24 Ethernet1 10.1.1.2 100
# ipv6 route 5001::/64 Ethernet1
# veos(config)#


- name: Gather the exisitng condiguration
  arista.eos.eos_static_routes:
    state: gathered

# returns :
#  arista.eos.eos_static_routes:
#    config:
#      - address_families:
#          - afi: ipv4
#            routes:
#              - dest: 165.10.1.0/24
#                next_hop:
#                  - forward_router_address: 10.1.1.2
#                    interface: "Ethernet1"
#                    admin_distance: 100
#          - afi: ipv6
#            routes:
#              - dest: 5001::/64
#                next_hop:
#                  - interface: "Ethernet1"


# Using rendered

#   arista.eos.eos_static_routes:
#    config:
#      - address_families:
#          - afi: ipv4
#            routes:
#              - dest: 165.10.1.0/24
#                next_hop:
#                  - forward_router_address: 10.1.1.2
#                    interface: "Ethernet1"
#                    admin_distance: 100
#         - afi: ipv6
#            routes:
#              - dest: 5001::/64
#                next_hop:
#                  - interface: "Ethernet1"

# returns:

# ip route 165.10.1.0/24 Ethernet1 10.1.1.2 100
# ipv6 route 5001::/64 Ethernet1


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - ip route vrf vrf1 192.2.2.0/24 125.2.3.1 93
rendered:
  description: The set of CLI commands generated from the value in C(config) option
  returned: When C(state) is I(rendered)
  type: list
  sample: >
    "address_families": [
                        {
                            "afi": "ipv4",
                            "routes": [
                                {
                                    "dest": "192.2.2.0/24",
                                    "next_hops": [
                                        {
                                            "admin_distance": 93,
                                            "description": null,
                                            "forward_router_address": null,
                                            "interface": "125.2.3.1",
                                            "mpls_label": null,
                                            "nexthop_grp": null,
                                            "tag": null,
                                            "track": null,
                                            "vrf": null
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "vrf": "vrf1"
                }
            ],
            "running_config": null,
            "state": "rendered"
        }
gathered:
  description: The configuration as structured data transformed for the running configuration
               fetched from remote host
  returned: When C(state) is I(gathered)
  type: list
  sample: >
    The configuration returned will always be in the same format
    of the parameters above.
parsed:
  description: The configuration as structured data transformed for the value of
               C(running_config) option
  returned: When C(state) is I(parsed)
  type: list
  sample: >
    The configuration returned will always be in the same format
    of the parameters above.
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.static_routes.static_routes import (
    Static_routesArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.static_routes.static_routes import (
    Static_routes,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """

    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=Static_routesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Static_routes(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()