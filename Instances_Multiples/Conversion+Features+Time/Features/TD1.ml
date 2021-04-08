<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <key id="d0" for="node" attr.name="bag" attr.type="string" />
  <graph edgedefault="undirected">

    <node id="n1">
      <data key="d0">c, e</data>
    </node>
    <node id="n2">
      <data key="d0">c</data>
    </node>
    <node id="n3">
      <data key="d0">c, d</data>
    </node>
    <node id="n4">
      <data key="d0">c</data>
    </node>
    <node id="n5">
      <data key="d0">b, c</data>
    </node>
    <node id="n6">
      <data key="d0">a, b, c</data>
    </node>

    <edge source="n1" target="n2"/>
    <edge source="n2" target="n3"/>
    <edge source="n3" target="n4"/>
    <edge source="n4" target="n5"/>
    <edge source="n5" target="n6"/>

  </graph>
</graphml>
