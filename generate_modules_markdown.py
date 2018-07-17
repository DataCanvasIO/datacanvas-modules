#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import re
import argparse
import io

def main():
    parser = argparse.ArgumentParser(description='Generate module markdown docs.')
    parser.add_argument('--root', metavar='root', nargs=1, help='root dir name')
    parser.add_argument('--dir', metavar='dir', nargs=1, help='subdir name')
    
    args = parser.parse_args()
    module_root_path = os.path.join(str(args.root[0]), str(args.dir[0]))
    sub_dir_name = str(args.dir[0])
    module_md_path = "docs/" + sub_dir_name + ".md"
    md_file = open(module_md_path, "w",encoding='utf-8')
    #md_file = io.open(module_md_path,'w',encoding=character_encoding)

    for root, dir, files in os.walk(module_root_path):
        for f in files:
            if f.endswith("_preset.json"):
                preset_path = os.path.join(root, f)
                module_name = re.sub('_preset.json', '', preset_path)
                o = json.loads(open(preset_path,encoding='utf-8').read())
                
                # print(module_name)
                md_file.write("\n")
                md_file.write("## %s\n" % o['name'])
                md_file.write("\n")
                md_file.write(str(o['description']))
                md_file.write("\n\n")
                md_file.write("#### Tag:\n")
                for tag in o['tagNames']:
                    md_file.write("* %s\n" % tag)
                md_file.write("\n")
                md_file.write("#### Param:\n")
                if len(o['param']) == 0:
                   md_file.write("* None\n")
                else:
                   for pk, pv in o['param'].items():
                    # print(pv)
                       md_file.write("* %s (%s) : %s\n" % (pk, pv['dataType'], pv.get('desc', '')))
                md_file.write("\n")
                md_file.write('#### Input:\n')
                if len(o['input']) == 0:
                	md_file.write("* None\n")
                else:
                	for pk, pv in o['input'].items():
                		md_file.write("* %s (%s) \n" % (pk, pv[0]))
                md_file.write("\n")
                md_file.write('#### Output:\n')
                if len(o['output']) == 0:
                	md_file.write("* None\n")
                else:
                	for pk, pv in o['output'].items():
                		md_file.write("* %s (%s) \n" % (pk, pv[0]))
                #md_file.write("\n")
                


if __name__ == "__main__":
    main()
