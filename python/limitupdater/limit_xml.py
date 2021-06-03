# -*- coding: utf-8 -*-
import xml.etree.ElementTree as Et


class LimitXml:
    def __init__(self, path):
        """
        存在结构如下的xml
        ```xml
<?xml version="1.0" encoding="GB2312"?>
<MachineTestStandard>
<MachineType>MediaTest 9508B</MachineType>
<ReleaseVersion>1.021</ReleaseVersion>
<ReleaseDate>2020/08/07</ReleaseDate>
<TestItems>
    <TestItem Name="White90Hz" ChromaType="Rvs">
        <AlgorithmItem Name="Chroma" Desc="Chroma">
            <TestStandards Desc="多媒体V6.0" ProductType="Noah" IsActive="1">
                <CriterionItem Name="CCT" ReverseName1="CCT" ReverseName2="CCTTolerance"
                               Desc="色温中心值" Remark="" Type="2" Range="[6000:8000]" />
                <CriterionItem Name="Cx" ReverseName1="C1" ReverseName2="C1Tolerance"
                               Desc="色坐标x" Remark="" Type="2" Range="[0.285:0.325]" />
                <CriterionItem Name="Cy" ReverseName1="C2" ReverseName2="C2Tolerance"
                               Desc="色坐标y" Remark="" Type="2" Range="[0.301:0.341]" />
            </TestStandards>
        </AlgorithmItem>
    </TestItem>
</TestItems>
</MachineTestStandard>
        ```
        则从中得到
        ```python
{'White90Hz': {'Chroma': {
                            'CCT': '[6000:8000]',
                            'Cx': '[0.285:0.325]',
                            'Cy': '[0.301:0.341]',
}}}
        ```
        :param path:
        :return:
        """
        self.path = path
        self.origin_root = None
        self.text = None
        self.read_limit_xml()
        # 格式化数据
        self.data = {}
        for test_item in self.origin_root.findall('.//TestItem[@Name]'):
            test_screen = test_item.get('Name')
            for algorithm_item in test_item.findall('.//AlgorithmItem[@Name]'):
                algorithm = algorithm_item.get('Name')
                for criterion_item in algorithm_item.findall('.//CriterionItem[@Name]'):
                    criterion = criterion_item.get('Name')
                    if 'Range' in criterion_item.keys():
                        limit = criterion_item.get('Range')
                    else:
                        limit = criterion_item.text
                    if limit:
                        self.data.setdefault(test_screen, {}) \
                            .setdefault(algorithm, {})[criterion] = [limit, None, None]
        return

    def read_limit_xml(self):
        """
        读取门限文件
        :return:
        """
        # 处理非UTF-8编码
        with open(self.path, 'rb') as fbobj:
            self.text = fbobj.readline()
            lsub = self.text.lower()
            if (
                b'encoding=' in lsub and
                not lsub[lsub.find(b'encoding=') + 10:].startswith(b'utf-8')
            ):
                # 有官方格式标签，类似`<?xml version="1.0" encoding="GB2312"?>`
                start = lsub.find(b'encoding=') + 10
                end = lsub.find(lsub[start - 1], start)  # self.text[start: end]为编码
                enc = self.text[start: end]
                # 重新读取
                fbobj.seek(0)
                self.text = fbobj.read()
                self.text = self.text[: start] + b'UTF-8' + self.text[end:]
                self.text = self.text.decode(enc.decode())
            else:
                # 未找到相关标签，按gbk处理
                fbobj.seek(0)
                self.text = fbobj.read()
                self.text = self.text.decode('GB2312')
            self.origin_root = Et.fromstring(self.text)
        return self

    def write_updated_xml(self, path):
        """
        将更改后的xml写到指定路径
        :param path:
        :return:
        """
        updated_root = Et.fromstring(self.text)
        for screen_item in updated_root.findall('.//TestItem[@Name]'):
            screen = screen_item.get('Name')
            if screen in self.data:
                screen_inner = self.data[screen]
                for algorithm_item in screen_item.findall('.//AlgorithmItem[@Name]'):
                    algorithm = algorithm_item.get('Name')
                    if algorithm in screen_inner:
                        algorithm_inner = screen_inner[algorithm]
                        for criterion_item in algorithm_item.findall('.//CriterionItem[@Name]'):
                            criterion = criterion_item.get('Name')
                            if criterion in algorithm_inner:
                                item_range = algorithm_inner[criterion]
                                # 存在修改
                                if item_range[2] or item_range[1]:
                                    updated_range = item_range[2] if item_range[2] else item_range[1]
                                    # 修改后与修改前有差别
                                    if updated_range != item_range[0]:
                                        if 'Range' in criterion_item.keys():
                                            criterion_item.set('Range', updated_range)
                                        else:
                                            criterion_item.text = updated_range
        Et.ElementTree(updated_root).write(path, encoding='GB2312')
        return self
