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
        try:
            self.root = Et.parse(path).getroot()
        except ValueError:
            # 处理非UTF-8编码
            with open(path, 'rb') as fbobj:
                text = fbobj.readline()
                lsub = text.lower()
                if (
                    b'encoding=' in lsub and
                    not lsub[lsub.find(b'encoding=') + 10:].startswith(b'utf-8')
                ):
                    # 有官方格式标签，类似`<?xml version="1.0" encoding="GB2312"?>`
                    start = lsub.find(b'encoding=') + 10
                    end = lsub.find(lsub[start - 1], start)  # text[start: end]为编码
                    enc = text[start: end]
                    # 重新读取
                    fbobj.seek(0)
                    text = fbobj.read()
                    text = text[: start] + b'UTF-8' + text[end:]
                    self.root = Et.fromstring(text.decode(enc.decode()))
                else:
                    # 未找到相关标签，按gbk处理
                    fbobj.seek(0)
                    text = fbobj.read()
                    self.root = Et.fromstring(text.decode('GBK'))
        # 格式化数据
        self.data = {}
        for test_item in self.root.findall('.//TestItem[@Name]'):
            test_screen = test_item.attrib['Name']
            for algorithm_item in test_item.findall('.//AlgorithmItem'):
                algorithm = algorithm_item.attrib['Name']
                for criterion_item in algorithm_item.findall('.//CriterionItem'):
                    criterion = criterion_item.attrib['Name']
                    if 'Range' in criterion_item.attrib:
                        limit = criterion_item.attrib['Range']
                    else:
                        limit = criterion_item.text
                    if limit:
                        self.data.setdefault(test_screen, {}) \
                            .setdefault(algorithm, {})[criterion] = [limit, None, None]
        return
