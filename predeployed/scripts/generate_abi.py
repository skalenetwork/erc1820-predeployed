#!/usr/bin/env python
from erc1820_predeployed import  ERC1820RegistryGenerator
import json


def main():
    print(json.dumps(ERC1820RegistryGenerator().get_abi(), sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
