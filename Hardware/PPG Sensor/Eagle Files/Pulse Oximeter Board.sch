<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.4.0">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="24" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="MAX30102EFD+">
<packages>
<package name="21-0880B">
<smd name="1" x="-1.3462" y="2.4" dx="0.8128" dy="0.254" layer="1"/>
<smd name="2" x="-1.3462" y="1.6" dx="0.8128" dy="0.254" layer="1"/>
<smd name="3" x="-1.3462" y="0.8" dx="0.8128" dy="0.254" layer="1"/>
<smd name="4" x="-1.3462" y="0" dx="0.8128" dy="0.254" layer="1"/>
<smd name="5" x="-1.3462" y="-0.799996875" dx="0.8128" dy="0.254" layer="1"/>
<smd name="6" x="-1.3462" y="-1.6" dx="0.8128" dy="0.254" layer="1"/>
<smd name="7" x="-1.3462" y="-2.4" dx="0.8128" dy="0.254" layer="1"/>
<smd name="8" x="1.3462" y="-2.4" dx="0.8128" dy="0.254" layer="1"/>
<smd name="9" x="1.3462" y="-1.6" dx="0.8128" dy="0.254" layer="1"/>
<smd name="10" x="1.3462" y="-0.8" dx="0.8128" dy="0.254" layer="1"/>
<smd name="11" x="1.3462" y="0" dx="0.8128" dy="0.254" layer="1"/>
<smd name="12" x="1.3462" y="0.799996875" dx="0.8128" dy="0.254" layer="1"/>
<smd name="13" x="1.3462" y="1.6" dx="0.8128" dy="0.254" layer="1"/>
<smd name="14" x="1.3462" y="2.4" dx="0.8128" dy="0.254" layer="1"/>
<wire x1="-2.0066" y1="-2.7686" x2="-2.0066" y2="2.7686" width="0.1524" layer="39"/>
<wire x1="-2.0066" y1="2.7686" x2="-1.7018" y2="2.7686" width="0.1524" layer="39"/>
<wire x1="2.0066" y1="2.7686" x2="1.7018" y2="2.7686" width="0.1524" layer="39"/>
<wire x1="2.0066" y1="2.7686" x2="2.0066" y2="-2.7686" width="0.1524" layer="39"/>
<wire x1="2.0066" y1="-2.7686" x2="1.7018" y2="-2.7686" width="0.1524" layer="39"/>
<wire x1="-2.0066" y1="-2.7686" x2="-1.7018" y2="-2.7686" width="0.1524" layer="39"/>
<wire x1="-1.7018" y1="-3.0988" x2="-1.7018" y2="-2.7686" width="0.1524" layer="39"/>
<wire x1="-1.7018" y1="2.7686" x2="-1.7018" y2="3.0988" width="0.1524" layer="39"/>
<wire x1="-1.7018" y1="3.0988" x2="1.7018" y2="3.0988" width="0.1524" layer="39"/>
<wire x1="1.7018" y1="3.0988" x2="1.7018" y2="2.7686" width="0.1524" layer="39"/>
<wire x1="1.7018" y1="-2.7686" x2="1.7018" y2="-3.0988" width="0.1524" layer="39"/>
<wire x1="1.7018" y1="-3.0988" x2="-1.7018" y2="-3.0988" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-2.0066" y="-2.781"/>
<vertex x="-2.0066" y="2.781"/>
<vertex x="-1.7018" y="2.781"/>
<vertex x="-1.7018" y="3.0988"/>
<vertex x="1.7018" y="3.0988"/>
<vertex x="1.7018" y="2.781"/>
<vertex x="2.0066" y="2.781"/>
<vertex x="2.0066" y="-2.781"/>
<vertex x="1.7018" y="-2.781"/>
<vertex x="1.7018" y="-3.0988"/>
<vertex x="-1.7018" y="-3.0988"/>
<vertex x="-1.7018" y="-2.781"/>
</polygon>
<wire x1="-1.5748" y1="-2.9718" x2="1.5748" y2="-2.9718" width="0.1524" layer="21"/>
<wire x1="1.5748" y1="2.9718" x2="-1.5748" y2="2.9718" width="0.1524" layer="21"/>
<wire x1="-2.1844" y1="2.3876" x2="-2.3368" y2="2.3876" width="0.1524" layer="21" curve="-180"/>
<wire x1="-2.3368" y1="2.3876" x2="-2.1844" y2="2.3876" width="0.1524" layer="21" curve="-180"/>
<wire x1="-1.4478" y1="-2.8448" x2="1.4478" y2="-2.8448" width="0.1524" layer="51"/>
<wire x1="1.4478" y1="-2.8448" x2="1.4478" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="1.4478" y1="2.8448" x2="0.3048" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="2.8448" x2="-0.3048" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="-0.3048" y1="2.8448" x2="-1.4478" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="-1.4478" y1="2.8448" x2="-1.4478" y2="-2.8448" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="2.3876" x2="-1.016" y2="2.3876" width="0.1524" layer="51" curve="-180"/>
<wire x1="-1.016" y1="2.3876" x2="-0.8636" y2="2.3876" width="0.1524" layer="51" curve="-180"/>
<wire x1="0.3048" y1="2.8448" x2="-0.3048" y2="2.8448" width="0.1524" layer="51" curve="-180"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="21-0880B-M">
<smd name="1" x="-1.397" y="2.4" dx="0.9144" dy="0.254" layer="1"/>
<smd name="2" x="-1.397" y="1.6" dx="0.9144" dy="0.254" layer="1"/>
<smd name="3" x="-1.397" y="0.8" dx="0.9144" dy="0.254" layer="1"/>
<smd name="4" x="-1.397" y="0" dx="0.9144" dy="0.254" layer="1"/>
<smd name="5" x="-1.397" y="-0.799996875" dx="0.9144" dy="0.254" layer="1"/>
<smd name="6" x="-1.397" y="-1.6" dx="0.9144" dy="0.254" layer="1"/>
<smd name="7" x="-1.397" y="-2.4" dx="0.9144" dy="0.254" layer="1"/>
<smd name="8" x="1.397" y="-2.4" dx="0.9144" dy="0.254" layer="1"/>
<smd name="9" x="1.397" y="-1.6" dx="0.9144" dy="0.254" layer="1"/>
<smd name="10" x="1.397" y="-0.8" dx="0.9144" dy="0.254" layer="1"/>
<smd name="11" x="1.397" y="0" dx="0.9144" dy="0.254" layer="1"/>
<smd name="12" x="1.397" y="0.799996875" dx="0.9144" dy="0.254" layer="1"/>
<smd name="13" x="1.397" y="1.6" dx="0.9144" dy="0.254" layer="1"/>
<smd name="14" x="1.397" y="2.4" dx="0.9144" dy="0.254" layer="1"/>
<wire x1="-2.3622" y1="-3.0226" x2="-2.3622" y2="3.0226" width="0.1524" layer="39"/>
<wire x1="-2.3622" y1="3.0226" x2="-1.9558" y2="3.0226" width="0.1524" layer="39"/>
<wire x1="2.3622" y1="3.0226" x2="1.9558" y2="3.0226" width="0.1524" layer="39"/>
<wire x1="2.3622" y1="3.0226" x2="2.3622" y2="-3.0226" width="0.1524" layer="39"/>
<wire x1="2.3622" y1="-3.0226" x2="1.9558" y2="-3.0226" width="0.1524" layer="39"/>
<wire x1="-2.3622" y1="-3.0226" x2="-1.9558" y2="-3.0226" width="0.1524" layer="39"/>
<wire x1="-1.9558" y1="-3.3528" x2="-1.9558" y2="-3.0226" width="0.1524" layer="39"/>
<wire x1="-1.9558" y1="3.0226" x2="-1.9558" y2="3.3528" width="0.1524" layer="39"/>
<wire x1="-1.9558" y1="3.3528" x2="1.9558" y2="3.3528" width="0.1524" layer="39"/>
<wire x1="1.9558" y1="3.3528" x2="1.9558" y2="3.0226" width="0.1524" layer="39"/>
<wire x1="1.9558" y1="-3.0226" x2="1.9558" y2="-3.3528" width="0.1524" layer="39"/>
<wire x1="1.9558" y1="-3.3528" x2="-1.9558" y2="-3.3528" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-2.3622" y="-3.035"/>
<vertex x="-2.3622" y="3.035"/>
<vertex x="-1.9558" y="3.035"/>
<vertex x="-1.9558" y="3.3528"/>
<vertex x="1.9558" y="3.3528"/>
<vertex x="1.9558" y="3.035"/>
<vertex x="2.3622" y="3.035"/>
<vertex x="2.3622" y="-3.035"/>
<vertex x="1.9558" y="-3.035"/>
<vertex x="1.9558" y="-3.3528"/>
<vertex x="-1.9558" y="-3.3528"/>
<vertex x="-1.9558" y="-3.035"/>
</polygon>
<wire x1="-1.5748" y1="-2.9718" x2="1.5748" y2="-2.9718" width="0.1524" layer="21"/>
<wire x1="1.5748" y1="2.9718" x2="-1.5748" y2="2.9718" width="0.1524" layer="21"/>
<wire x1="-2.286" y1="2.3876" x2="-2.4384" y2="2.3876" width="0.1524" layer="21" curve="-180"/>
<wire x1="-2.4384" y1="2.3876" x2="-2.286" y2="2.3876" width="0.1524" layer="21" curve="-180"/>
<wire x1="-1.4478" y1="-2.8448" x2="1.4478" y2="-2.8448" width="0.1524" layer="51"/>
<wire x1="1.4478" y1="-2.8448" x2="1.4478" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="1.4478" y1="2.8448" x2="0.3048" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="2.8448" x2="-0.3048" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="-0.3048" y1="2.8448" x2="-1.4478" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="-1.4478" y1="2.8448" x2="-1.4478" y2="-2.8448" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="2.3876" x2="-1.016" y2="2.3876" width="0.1524" layer="51" curve="-180"/>
<wire x1="-1.016" y1="2.3876" x2="-0.8636" y2="2.3876" width="0.1524" layer="51" curve="-180"/>
<wire x1="0.3048" y1="2.8448" x2="-0.3048" y2="2.8448" width="0.1524" layer="51" curve="-180"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="21-0880B-L">
<smd name="1" x="-1.2954" y="2.4" dx="0.7112" dy="0.254" layer="1"/>
<smd name="2" x="-1.2954" y="1.6" dx="0.7112" dy="0.254" layer="1"/>
<smd name="3" x="-1.2954" y="0.8" dx="0.7112" dy="0.254" layer="1"/>
<smd name="4" x="-1.2954" y="0" dx="0.7112" dy="0.254" layer="1"/>
<smd name="5" x="-1.2954" y="-0.799996875" dx="0.7112" dy="0.254" layer="1"/>
<smd name="6" x="-1.2954" y="-1.6" dx="0.7112" dy="0.254" layer="1"/>
<smd name="7" x="-1.2954" y="-2.4" dx="0.7112" dy="0.254" layer="1"/>
<smd name="8" x="1.2954" y="-2.4" dx="0.7112" dy="0.254" layer="1"/>
<smd name="9" x="1.2954" y="-1.6" dx="0.7112" dy="0.254" layer="1"/>
<smd name="10" x="1.2954" y="-0.8" dx="0.7112" dy="0.254" layer="1"/>
<smd name="11" x="1.2954" y="0" dx="0.7112" dy="0.254" layer="1"/>
<smd name="12" x="1.2954" y="0.799996875" dx="0.7112" dy="0.254" layer="1"/>
<smd name="13" x="1.2954" y="1.6" dx="0.7112" dy="0.254" layer="1"/>
<smd name="14" x="1.2954" y="2.4" dx="0.7112" dy="0.254" layer="1"/>
<wire x1="-1.7526" y1="-2.6162" x2="-1.7526" y2="2.6162" width="0.1524" layer="39"/>
<wire x1="-1.7526" y1="2.6162" x2="-1.5494" y2="2.6162" width="0.1524" layer="39"/>
<wire x1="1.7526" y1="2.6162" x2="1.5494" y2="2.6162" width="0.1524" layer="39"/>
<wire x1="1.7526" y1="2.6162" x2="1.7526" y2="-2.6162" width="0.1524" layer="39"/>
<wire x1="1.7526" y1="-2.6162" x2="1.5494" y2="-2.6162" width="0.1524" layer="39"/>
<wire x1="-1.7526" y1="-2.6162" x2="-1.5494" y2="-2.6162" width="0.1524" layer="39"/>
<wire x1="-1.5494" y1="-2.9464" x2="-1.5494" y2="-2.6162" width="0.1524" layer="39"/>
<wire x1="-1.5494" y1="2.6162" x2="-1.5494" y2="2.9464" width="0.1524" layer="39"/>
<wire x1="-1.5494" y1="2.9464" x2="1.5494" y2="2.9464" width="0.1524" layer="39"/>
<wire x1="1.5494" y1="2.9464" x2="1.5494" y2="2.6162" width="0.1524" layer="39"/>
<wire x1="1.5494" y1="-2.6162" x2="1.5494" y2="-2.9464" width="0.1524" layer="39"/>
<wire x1="1.5494" y1="-2.9464" x2="-1.5494" y2="-2.9464" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-1.7526" y="-2.6286"/>
<vertex x="-1.7526" y="2.6286"/>
<vertex x="-1.5494" y="2.6286"/>
<vertex x="-1.5494" y="2.9464"/>
<vertex x="1.5494" y="2.9464"/>
<vertex x="1.5494" y="2.6286"/>
<vertex x="1.7526" y="2.6286"/>
<vertex x="1.7526" y="-2.6286"/>
<vertex x="1.5494" y="-2.6286"/>
<vertex x="1.5494" y="-2.9464"/>
<vertex x="-1.5494" y="-2.9464"/>
<vertex x="-1.5494" y="-2.6286"/>
</polygon>
<wire x1="-1.5748" y1="-2.9718" x2="1.5748" y2="-2.9718" width="0.1524" layer="21"/>
<wire x1="1.5748" y1="2.9718" x2="-1.5748" y2="2.9718" width="0.1524" layer="21"/>
<wire x1="-2.0828" y1="2.3876" x2="-2.2352" y2="2.3876" width="0.1524" layer="21" curve="-180"/>
<wire x1="-2.2352" y1="2.3876" x2="-2.0828" y2="2.3876" width="0.1524" layer="21" curve="-180"/>
<wire x1="-1.4478" y1="-2.8448" x2="1.4478" y2="-2.8448" width="0.1524" layer="51"/>
<wire x1="1.4478" y1="-2.8448" x2="1.4478" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="1.4478" y1="2.8448" x2="0.3048" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="2.8448" x2="-0.3048" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="-0.3048" y1="2.8448" x2="-1.4478" y2="2.8448" width="0.1524" layer="51"/>
<wire x1="-1.4478" y1="2.8448" x2="-1.4478" y2="-2.8448" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="2.3876" x2="-1.016" y2="2.3876" width="0.1524" layer="51" curve="-180"/>
<wire x1="-1.016" y1="2.3876" x2="-0.8636" y2="2.3876" width="0.1524" layer="51" curve="-180"/>
<wire x1="0.3048" y1="2.8448" x2="-0.3048" y2="2.8448" width="0.1524" layer="51" curve="-180"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
</packages>
<symbols>
<symbol name="MAX30102EFD+">
<pin name="N.C._2" x="2.54" y="0" length="middle" direction="nc"/>
<pin name="SCL" x="2.54" y="-5.08" length="middle" direction="in"/>
<pin name="SDA" x="2.54" y="-10.16" length="middle"/>
<pin name="PGND" x="2.54" y="-15.24" length="middle" direction="pwr"/>
<pin name="R_DRV" x="2.54" y="-20.32" length="middle" direction="pas"/>
<pin name="IR_DRV" x="2.54" y="-25.4" length="middle" direction="pas"/>
<pin name="N.C._3" x="2.54" y="-30.48" length="middle" direction="nc"/>
<pin name="N.C._4" x="63.5" y="-30.48" length="middle" direction="nc" rot="R180"/>
<pin name="VLED+_2" x="63.5" y="-25.4" length="middle" direction="pas" rot="R180"/>
<pin name="VLED+" x="63.5" y="-20.32" length="middle" direction="pas" rot="R180"/>
<pin name="VDD" x="63.5" y="-15.24" length="middle" direction="pwr" rot="R180"/>
<pin name="GND" x="63.5" y="-10.16" length="middle" direction="pwr" rot="R180"/>
<pin name="!INT" x="63.5" y="-5.08" length="middle" direction="pas" rot="R180"/>
<pin name="N.C." x="63.5" y="0" length="middle" direction="nc" rot="R180"/>
<wire x1="7.62" y1="10.16" x2="7.62" y2="-40.64" width="0.1524" layer="94"/>
<wire x1="7.62" y1="-40.64" x2="58.42" y2="-40.64" width="0.1524" layer="94"/>
<wire x1="58.42" y1="-40.64" x2="58.42" y2="10.16" width="0.1524" layer="94"/>
<wire x1="58.42" y1="10.16" x2="7.62" y2="10.16" width="0.1524" layer="94"/>
<text x="28.2956" y="19.2786" size="2.0828" layer="95" ratio="6" rot="SR0">&gt;Name</text>
<text x="27.6606" y="14.1986" size="2.0828" layer="96" ratio="6" rot="SR0">&gt;Value</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="MAX30102EFD+" prefix="U">
<gates>
<gate name="A" symbol="MAX30102EFD+" x="0" y="0"/>
</gates>
<devices>
<device name="" package="21-0880B">
<connects>
<connect gate="A" pin="!INT" pad="13"/>
<connect gate="A" pin="GND" pad="12"/>
<connect gate="A" pin="IR_DRV" pad="6"/>
<connect gate="A" pin="N.C." pad="14"/>
<connect gate="A" pin="N.C._2" pad="1"/>
<connect gate="A" pin="N.C._3" pad="7"/>
<connect gate="A" pin="N.C._4" pad="8"/>
<connect gate="A" pin="PGND" pad="4"/>
<connect gate="A" pin="R_DRV" pad="5"/>
<connect gate="A" pin="SCL" pad="2"/>
<connect gate="A" pin="SDA" pad="3"/>
<connect gate="A" pin="VDD" pad="11"/>
<connect gate="A" pin="VLED+" pad="10"/>
<connect gate="A" pin="VLED+_2" pad="9"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="MAX30102EFD+" constant="no"/>
<attribute name="VENDOR" value="Maxim Integrated Products" constant="no"/>
</technology>
</technologies>
</device>
<device name="21-0880B-M" package="21-0880B-M">
<connects>
<connect gate="A" pin="!INT" pad="13"/>
<connect gate="A" pin="GND" pad="12"/>
<connect gate="A" pin="IR_DRV" pad="6"/>
<connect gate="A" pin="N.C." pad="14"/>
<connect gate="A" pin="N.C._2" pad="1"/>
<connect gate="A" pin="N.C._3" pad="7"/>
<connect gate="A" pin="N.C._4" pad="8"/>
<connect gate="A" pin="PGND" pad="4"/>
<connect gate="A" pin="R_DRV" pad="5"/>
<connect gate="A" pin="SCL" pad="2"/>
<connect gate="A" pin="SDA" pad="3"/>
<connect gate="A" pin="VDD" pad="11"/>
<connect gate="A" pin="VLED+" pad="10"/>
<connect gate="A" pin="VLED+_2" pad="9"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="MAX30102EFD+" constant="no"/>
<attribute name="VENDOR" value="Maxim Integrated Products" constant="no"/>
</technology>
</technologies>
</device>
<device name="21-0880B-L" package="21-0880B-L">
<connects>
<connect gate="A" pin="!INT" pad="13"/>
<connect gate="A" pin="GND" pad="12"/>
<connect gate="A" pin="IR_DRV" pad="6"/>
<connect gate="A" pin="N.C." pad="14"/>
<connect gate="A" pin="N.C._2" pad="1"/>
<connect gate="A" pin="N.C._3" pad="7"/>
<connect gate="A" pin="N.C._4" pad="8"/>
<connect gate="A" pin="PGND" pad="4"/>
<connect gate="A" pin="R_DRV" pad="5"/>
<connect gate="A" pin="SCL" pad="2"/>
<connect gate="A" pin="SDA" pad="3"/>
<connect gate="A" pin="VDD" pad="11"/>
<connect gate="A" pin="VLED+" pad="10"/>
<connect gate="A" pin="VLED+_2" pad="9"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="MAX30102EFD+" constant="no"/>
<attribute name="VENDOR" value="Maxim Integrated Products" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="MAX14595ETA+">
<packages>
<package name="21-0487A">
<smd name="1" x="-0.9525" y="0.75" dx="0.762" dy="0.2032" layer="1"/>
<smd name="2" x="-0.9525" y="0.25" dx="0.762" dy="0.2032" layer="1"/>
<smd name="3" x="-0.9525" y="-0.25" dx="0.762" dy="0.2032" layer="1"/>
<smd name="4" x="-0.9525" y="-0.75" dx="0.762" dy="0.2032" layer="1"/>
<smd name="5" x="0.9525" y="-0.75" dx="0.762" dy="0.2032" layer="1"/>
<smd name="6" x="0.9525" y="-0.25" dx="0.762" dy="0.2032" layer="1"/>
<smd name="7" x="0.9525" y="0.25" dx="0.762" dy="0.2032" layer="1"/>
<smd name="8" x="0.9525" y="0.75" dx="0.762" dy="0.2032" layer="1"/>
<wire x1="-1.5748" y1="-1.1176" x2="-1.5748" y2="1.1176" width="0.1524" layer="39"/>
<wire x1="-1.5748" y1="1.1176" x2="-1.27" y2="1.1176" width="0.1524" layer="39"/>
<wire x1="1.5748" y1="1.1176" x2="1.27" y2="1.1176" width="0.1524" layer="39"/>
<wire x1="1.5748" y1="1.1176" x2="1.5748" y2="-1.1176" width="0.1524" layer="39"/>
<wire x1="1.5748" y1="-1.1176" x2="1.27" y2="-1.1176" width="0.1524" layer="39"/>
<wire x1="-1.5748" y1="-1.1176" x2="-1.27" y2="-1.1176" width="0.1524" layer="39"/>
<wire x1="-1.27" y1="-1.27" x2="-1.27" y2="-1.1176" width="0.1524" layer="39"/>
<wire x1="-1.27" y1="1.1176" x2="-1.27" y2="1.27" width="0.1524" layer="39"/>
<wire x1="-1.27" y1="1.27" x2="1.27" y2="1.27" width="0.1524" layer="39"/>
<wire x1="1.27" y1="1.27" x2="1.27" y2="1.1176" width="0.1524" layer="39"/>
<wire x1="1.27" y1="-1.1176" x2="1.27" y2="-1.27" width="0.1524" layer="39"/>
<wire x1="1.27" y1="-1.27" x2="-1.27" y2="-1.27" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-1.5875" y="-1.1056"/>
<vertex x="-1.5875" y="1.1056"/>
<vertex x="-1.2827" y="1.1056"/>
<vertex x="-1.2827" y="1.2827"/>
<vertex x="1.2827" y="1.2827"/>
<vertex x="1.2827" y="1.1056"/>
<vertex x="1.5875" y="1.1056"/>
<vertex x="1.5875" y="-1.1056"/>
<vertex x="1.2827" y="-1.1056"/>
<vertex x="1.2827" y="-1.2827"/>
<vertex x="-1.2827" y="-1.2827"/>
<vertex x="-1.2827" y="-1.1056"/>
</polygon>
<wire x1="-0.4318" y1="-1.1684" x2="0.4318" y2="-1.1684" width="0.1524" layer="21"/>
<wire x1="0.4318" y1="1.1684" x2="-0.4318" y2="1.1684" width="0.1524" layer="21"/>
<wire x1="-1.6764" y1="0.6858" x2="-1.6764" y2="0.8128" width="0.1524" layer="21" curve="-208"/>
<wire x1="-1.016" y1="-1.016" x2="1.016" y2="-1.016" width="0.1524" layer="51"/>
<wire x1="1.016" y1="-1.016" x2="1.016" y2="1.016" width="0.1524" layer="51"/>
<wire x1="1.016" y1="1.016" x2="-1.016" y2="1.016" width="0.1524" layer="51"/>
<wire x1="-1.016" y1="1.016" x2="-1.016" y2="-1.016" width="0.1524" layer="51"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="21-0487A-M">
<smd name="1" x="-1.0033" y="0.75" dx="0.8636" dy="0.2032" layer="1"/>
<smd name="2" x="-1.0033" y="0.25" dx="0.8636" dy="0.2032" layer="1"/>
<smd name="3" x="-1.0033" y="-0.25" dx="0.8636" dy="0.2032" layer="1"/>
<smd name="4" x="-1.0033" y="-0.75" dx="0.8636" dy="0.2032" layer="1"/>
<smd name="5" x="1.0033" y="-0.75" dx="0.8636" dy="0.2032" layer="1"/>
<smd name="6" x="1.0033" y="-0.25" dx="0.8636" dy="0.2032" layer="1"/>
<smd name="7" x="1.0033" y="0.25" dx="0.8636" dy="0.2032" layer="1"/>
<smd name="8" x="1.0033" y="0.75" dx="0.8636" dy="0.2032" layer="1"/>
<wire x1="-1.9304" y1="-1.3716" x2="-1.9304" y2="1.3716" width="0.1524" layer="39"/>
<wire x1="-1.9304" y1="1.3716" x2="-1.524" y2="1.3716" width="0.1524" layer="39"/>
<wire x1="1.9304" y1="1.3716" x2="1.524" y2="1.3716" width="0.1524" layer="39"/>
<wire x1="1.9304" y1="1.3716" x2="1.9304" y2="-1.3716" width="0.1524" layer="39"/>
<wire x1="1.9304" y1="-1.3716" x2="1.524" y2="-1.3716" width="0.1524" layer="39"/>
<wire x1="-1.9304" y1="-1.3716" x2="-1.524" y2="-1.3716" width="0.1524" layer="39"/>
<wire x1="-1.524" y1="-1.524" x2="-1.524" y2="-1.3716" width="0.1524" layer="39"/>
<wire x1="-1.524" y1="1.3716" x2="-1.524" y2="1.524" width="0.1524" layer="39"/>
<wire x1="-1.524" y1="1.524" x2="1.524" y2="1.524" width="0.1524" layer="39"/>
<wire x1="1.524" y1="1.524" x2="1.524" y2="1.3716" width="0.1524" layer="39"/>
<wire x1="1.524" y1="-1.3716" x2="1.524" y2="-1.524" width="0.1524" layer="39"/>
<wire x1="1.524" y1="-1.524" x2="-1.524" y2="-1.524" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-1.9431" y="-1.3596"/>
<vertex x="-1.9431" y="1.3596"/>
<vertex x="-1.5367" y="1.3596"/>
<vertex x="-1.5367" y="1.5367"/>
<vertex x="1.5367" y="1.5367"/>
<vertex x="1.5367" y="1.3596"/>
<vertex x="1.9431" y="1.3596"/>
<vertex x="1.9431" y="-1.3596"/>
<vertex x="1.5367" y="-1.3596"/>
<vertex x="1.5367" y="-1.5367"/>
<vertex x="-1.5367" y="-1.5367"/>
<vertex x="-1.5367" y="-1.3596"/>
</polygon>
<wire x1="-0.4318" y1="-1.1684" x2="0.4318" y2="-1.1684" width="0.1524" layer="21"/>
<wire x1="0.4318" y1="1.1684" x2="-0.4318" y2="1.1684" width="0.1524" layer="21"/>
<wire x1="-1.778" y1="0.6858" x2="-1.778" y2="0.8128" width="0.1524" layer="21" curve="-208"/>
<wire x1="-1.016" y1="-1.016" x2="1.016" y2="-1.016" width="0.1524" layer="51"/>
<wire x1="1.016" y1="-1.016" x2="1.016" y2="1.016" width="0.1524" layer="51"/>
<wire x1="1.016" y1="1.016" x2="-1.016" y2="1.016" width="0.1524" layer="51"/>
<wire x1="-1.016" y1="1.016" x2="-1.016" y2="-1.016" width="0.1524" layer="51"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="21-0487A-L">
<smd name="1" x="-0.9017" y="0.75" dx="0.6604" dy="0.2032" layer="1"/>
<smd name="2" x="-0.9017" y="0.25" dx="0.6604" dy="0.2032" layer="1"/>
<smd name="3" x="-0.9017" y="-0.25" dx="0.6604" dy="0.2032" layer="1"/>
<smd name="4" x="-0.9017" y="-0.75" dx="0.6604" dy="0.2032" layer="1"/>
<smd name="5" x="0.9017" y="-0.75" dx="0.6604" dy="0.2032" layer="1"/>
<smd name="6" x="0.9017" y="-0.25" dx="0.6604" dy="0.2032" layer="1"/>
<smd name="7" x="0.9017" y="0.25" dx="0.6604" dy="0.2032" layer="1"/>
<smd name="8" x="0.9017" y="0.75" dx="0.6604" dy="0.2032" layer="1"/>
<wire x1="-1.3208" y1="-0.9652" x2="-1.3208" y2="0.9652" width="0.1524" layer="39"/>
<wire x1="-1.3208" y1="0.9652" x2="-1.1176" y2="0.9652" width="0.1524" layer="39"/>
<wire x1="1.3208" y1="0.9652" x2="1.1176" y2="0.9652" width="0.1524" layer="39"/>
<wire x1="1.3208" y1="0.9652" x2="1.3208" y2="-0.9652" width="0.1524" layer="39"/>
<wire x1="1.3208" y1="-0.9652" x2="1.1176" y2="-0.9652" width="0.1524" layer="39"/>
<wire x1="-1.3208" y1="-0.9652" x2="-1.1176" y2="-0.9652" width="0.1524" layer="39"/>
<wire x1="-1.1176" y1="-1.1176" x2="-1.1176" y2="-0.9652" width="0.1524" layer="39"/>
<wire x1="-1.1176" y1="0.9652" x2="-1.1176" y2="1.1176" width="0.1524" layer="39"/>
<wire x1="-1.1176" y1="1.1176" x2="1.1176" y2="1.1176" width="0.1524" layer="39"/>
<wire x1="1.1176" y1="1.1176" x2="1.1176" y2="0.9652" width="0.1524" layer="39"/>
<wire x1="1.1176" y1="-0.9652" x2="1.1176" y2="-1.1176" width="0.1524" layer="39"/>
<wire x1="1.1176" y1="-1.1176" x2="-1.1176" y2="-1.1176" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-1.3335" y="-0.9532"/>
<vertex x="-1.3335" y="0.9532"/>
<vertex x="-1.1303" y="0.9532"/>
<vertex x="-1.1303" y="1.1303"/>
<vertex x="1.1303" y="1.1303"/>
<vertex x="1.1303" y="0.9532"/>
<vertex x="1.3335" y="0.9532"/>
<vertex x="1.3335" y="-0.9532"/>
<vertex x="1.1303" y="-0.9532"/>
<vertex x="1.1303" y="-1.1303"/>
<vertex x="-1.1303" y="-1.1303"/>
<vertex x="-1.1303" y="-0.9532"/>
</polygon>
<wire x1="-0.4318" y1="-1.1684" x2="0.4318" y2="-1.1684" width="0.1524" layer="21"/>
<wire x1="0.4318" y1="1.1684" x2="-0.4318" y2="1.1684" width="0.1524" layer="21"/>
<wire x1="-1.5748" y1="0.6858" x2="-1.5748" y2="0.8128" width="0.1524" layer="21" curve="-208"/>
<wire x1="-1.016" y1="-1.016" x2="1.016" y2="-1.016" width="0.1524" layer="51"/>
<wire x1="1.016" y1="-1.016" x2="1.016" y2="1.016" width="0.1524" layer="51"/>
<wire x1="1.016" y1="1.016" x2="-1.016" y2="1.016" width="0.1524" layer="51"/>
<wire x1="-1.016" y1="1.016" x2="-1.016" y2="-1.016" width="0.1524" layer="51"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
</packages>
<symbols>
<symbol name="MAX14595ETA+">
<pin name="VL" x="2.54" y="0" length="middle" direction="pwr"/>
<pin name="IOVL2" x="2.54" y="-2.54" length="middle" direction="pas"/>
<pin name="IOVL1" x="2.54" y="-5.08" length="middle" direction="pas"/>
<pin name="!TS" x="2.54" y="-7.62" length="middle" direction="pas"/>
<pin name="GND" x="63.5" y="-7.62" length="middle" direction="pwr" rot="R180"/>
<pin name="IOVCC1" x="63.5" y="-5.08" length="middle" direction="pas" rot="R180"/>
<pin name="IOVCC2" x="63.5" y="-2.54" length="middle" direction="pas" rot="R180"/>
<pin name="VCC" x="63.5" y="0" length="middle" direction="pwr" rot="R180"/>
<wire x1="7.62" y1="5.08" x2="7.62" y2="-12.7" width="0.1524" layer="94"/>
<wire x1="7.62" y1="-12.7" x2="58.42" y2="-12.7" width="0.1524" layer="94"/>
<wire x1="58.42" y1="-12.7" x2="58.42" y2="5.08" width="0.1524" layer="94"/>
<wire x1="58.42" y1="5.08" x2="7.62" y2="5.08" width="0.1524" layer="94"/>
<text x="28.2956" y="9.1186" size="2.0828" layer="95" ratio="6" rot="SR0">&gt;Name</text>
<text x="27.6606" y="6.5786" size="2.0828" layer="96" ratio="6" rot="SR0">&gt;Value</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="MAX14595ETA+" prefix="U">
<gates>
<gate name="A" symbol="MAX14595ETA+" x="0" y="0"/>
</gates>
<devices>
<device name="" package="21-0487A">
<connects>
<connect gate="A" pin="!TS" pad="4"/>
<connect gate="A" pin="GND" pad="5"/>
<connect gate="A" pin="IOVCC1" pad="6"/>
<connect gate="A" pin="IOVCC2" pad="7"/>
<connect gate="A" pin="IOVL1" pad="3"/>
<connect gate="A" pin="IOVL2" pad="2"/>
<connect gate="A" pin="VCC" pad="8"/>
<connect gate="A" pin="VL" pad="1"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="MAX14595ETA+" constant="no"/>
<attribute name="VENDOR" value="Maxim Integrated Products" constant="no"/>
</technology>
</technologies>
</device>
<device name="21-0487A-M" package="21-0487A-M">
<connects>
<connect gate="A" pin="!TS" pad="4"/>
<connect gate="A" pin="GND" pad="5"/>
<connect gate="A" pin="IOVCC1" pad="6"/>
<connect gate="A" pin="IOVCC2" pad="7"/>
<connect gate="A" pin="IOVL1" pad="3"/>
<connect gate="A" pin="IOVL2" pad="2"/>
<connect gate="A" pin="VCC" pad="8"/>
<connect gate="A" pin="VL" pad="1"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="MAX14595ETA+" constant="no"/>
<attribute name="VENDOR" value="Maxim Integrated Products" constant="no"/>
</technology>
</technologies>
</device>
<device name="21-0487A-L" package="21-0487A-L">
<connects>
<connect gate="A" pin="!TS" pad="4"/>
<connect gate="A" pin="GND" pad="5"/>
<connect gate="A" pin="IOVCC1" pad="6"/>
<connect gate="A" pin="IOVCC2" pad="7"/>
<connect gate="A" pin="IOVL1" pad="3"/>
<connect gate="A" pin="IOVL2" pad="2"/>
<connect gate="A" pin="VCC" pad="8"/>
<connect gate="A" pin="VL" pad="1"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="MAX14595ETA+" constant="no"/>
<attribute name="VENDOR" value="Maxim Integrated Products" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="MAX1921EUT18+">
<packages>
<package name="21-0058I">
<smd name="1" x="-1.1938" y="0.95" dx="1.3208" dy="0.5588" layer="1"/>
<smd name="2" x="-1.1938" y="0" dx="1.3208" dy="0.5588" layer="1"/>
<smd name="3" x="-1.1938" y="-0.95" dx="1.3208" dy="0.5588" layer="1"/>
<smd name="4" x="1.1938" y="-0.95" dx="1.3208" dy="0.5588" layer="1"/>
<smd name="5" x="1.1938" y="0" dx="1.3208" dy="0.5588" layer="1"/>
<smd name="6" x="1.1938" y="0.95" dx="1.3208" dy="0.5588" layer="1"/>
<wire x1="-0.8636" y1="0.6858" x2="-0.889" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="-0.889" y1="1.1938" x2="-1.4986" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="1.1938" x2="-1.4986" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="0.6858" x2="-0.8636" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-0.254" x2="-0.889" y2="0.254" width="0.1524" layer="51"/>
<wire x1="-0.889" y1="0.254" x2="-1.4986" y2="0.254" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="0.254" x2="-1.4986" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="-0.254" x2="-0.8636" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-1.1938" x2="-0.8636" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-0.6858" x2="-1.4986" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="-0.6858" x2="-1.4986" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="-1.1938" x2="-0.8636" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="-0.6858" x2="0.889" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="0.889" y1="-1.1938" x2="1.4986" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="-1.1938" x2="1.4986" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="-0.6858" x2="0.8636" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="0.254" x2="0.8636" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="-0.254" x2="1.4986" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="-0.254" x2="1.4986" y2="0.254" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="0.254" x2="0.8636" y2="0.254" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="1.1938" x2="0.8636" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="0.6858" x2="1.4986" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="0.6858" x2="1.4986" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="1.1938" x2="0.8636" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-1.4986" x2="0.8636" y2="-1.4986" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="-1.4986" x2="0.8636" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="1.4986" x2="0.3048" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="-0.3048" y1="1.4986" x2="-0.8636" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="1.4986" x2="-0.8636" y2="-1.4986" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0.1524" layer="51" curve="-180"/>
<text x="-1.0668" y="0.1524" size="1.27" layer="51" ratio="6" rot="SR0">*</text>
<wire x1="-2.1082" y1="-1.4732" x2="-2.1082" y2="1.4732" width="0.1524" layer="39"/>
<wire x1="-2.1082" y1="1.4732" x2="-1.1176" y2="1.4732" width="0.1524" layer="39"/>
<wire x1="-1.1176" y1="1.4732" x2="-1.1176" y2="1.7526" width="0.1524" layer="39"/>
<wire x1="-1.1176" y1="1.7526" x2="1.1176" y2="1.7526" width="0.1524" layer="39"/>
<wire x1="1.1176" y1="1.7526" x2="1.1176" y2="1.4732" width="0.1524" layer="39"/>
<wire x1="2.1082" y1="1.4732" x2="1.1176" y2="1.4732" width="0.1524" layer="39"/>
<wire x1="2.1082" y1="1.4732" x2="2.1082" y2="-1.4732" width="0.1524" layer="39"/>
<wire x1="2.1082" y1="-1.4732" x2="1.1176" y2="-1.4732" width="0.1524" layer="39"/>
<wire x1="1.1176" y1="-1.4732" x2="1.1176" y2="-1.7526" width="0.1524" layer="39"/>
<wire x1="1.1176" y1="-1.7526" x2="-1.1176" y2="-1.7526" width="0.1524" layer="39"/>
<wire x1="-1.1176" y1="-1.7526" x2="-1.1176" y2="-1.4732" width="0.1524" layer="39"/>
<wire x1="-2.1082" y1="-1.4732" x2="-1.1176" y2="-1.4732" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-2.1082" y="-1.4834"/>
<vertex x="-2.1082" y="1.4834"/>
<vertex x="-1.1303" y="1.4834"/>
<vertex x="-1.1303" y="1.7526"/>
<vertex x="1.1303" y="1.7526"/>
<vertex x="1.1303" y="1.4834"/>
<vertex x="2.1082" y="1.4834"/>
<vertex x="2.1082" y="-1.4834"/>
<vertex x="1.1303" y="-1.4834"/>
<vertex x="1.1303" y="-1.7526"/>
<vertex x="-1.1303" y="-1.7526"/>
<vertex x="-1.1303" y="-1.4834"/>
</polygon>
<wire x1="-1.016" y1="-1.6256" x2="1.016" y2="-1.6256" width="0.1524" layer="21"/>
<wire x1="1.016" y1="1.6256" x2="-1.016" y2="1.6256" width="0.1524" layer="21"/>
<text x="-2.032" y="1.3716" size="1.27" layer="21" ratio="6" rot="SR0">*</text>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="21-0058I-M">
<smd name="1" x="-1.2446" y="0.95" dx="1.6256" dy="0.6096" layer="1"/>
<smd name="2" x="-1.2446" y="0" dx="1.6256" dy="0.6096" layer="1"/>
<smd name="3" x="-1.2446" y="-0.95" dx="1.6256" dy="0.6096" layer="1"/>
<smd name="4" x="1.2446" y="-0.95" dx="1.6256" dy="0.6096" layer="1"/>
<smd name="5" x="1.2446" y="0" dx="1.6256" dy="0.6096" layer="1"/>
<smd name="6" x="1.2446" y="0.95" dx="1.6256" dy="0.6096" layer="1"/>
<wire x1="-0.8636" y1="0.6858" x2="-0.889" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="-0.889" y1="1.1938" x2="-1.4986" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="1.1938" x2="-1.4986" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="0.6858" x2="-0.8636" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-0.254" x2="-0.889" y2="0.254" width="0.1524" layer="51"/>
<wire x1="-0.889" y1="0.254" x2="-1.4986" y2="0.254" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="0.254" x2="-1.4986" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="-0.254" x2="-0.8636" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-1.1938" x2="-0.8636" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-0.6858" x2="-1.4986" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="-0.6858" x2="-1.4986" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="-1.1938" x2="-0.8636" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="-0.6858" x2="0.889" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="0.889" y1="-1.1938" x2="1.4986" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="-1.1938" x2="1.4986" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="-0.6858" x2="0.8636" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="0.254" x2="0.8636" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="-0.254" x2="1.4986" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="-0.254" x2="1.4986" y2="0.254" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="0.254" x2="0.8636" y2="0.254" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="1.1938" x2="0.8636" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="0.6858" x2="1.4986" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="0.6858" x2="1.4986" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="1.1938" x2="0.8636" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-1.4986" x2="0.8636" y2="-1.4986" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="-1.4986" x2="0.8636" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="1.4986" x2="0.3048" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="-0.3048" y1="1.4986" x2="-0.8636" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="1.4986" x2="-0.8636" y2="-1.4986" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0.1524" layer="51" curve="-180"/>
<text x="-1.0668" y="0.1524" size="1.27" layer="51" ratio="6" rot="SR0">*</text>
<wire x1="-2.5654" y1="-1.7526" x2="-2.5654" y2="1.7526" width="0.1524" layer="39"/>
<wire x1="-2.5654" y1="1.7526" x2="-1.3716" y2="1.7526" width="0.1524" layer="39"/>
<wire x1="-1.3716" y1="1.7526" x2="-1.3716" y2="2.0066" width="0.1524" layer="39"/>
<wire x1="-1.3716" y1="2.0066" x2="1.3716" y2="2.0066" width="0.1524" layer="39"/>
<wire x1="1.3716" y1="2.0066" x2="1.3716" y2="1.7526" width="0.1524" layer="39"/>
<wire x1="2.5654" y1="1.7526" x2="1.3716" y2="1.7526" width="0.1524" layer="39"/>
<wire x1="2.5654" y1="1.7526" x2="2.5654" y2="-1.7526" width="0.1524" layer="39"/>
<wire x1="2.5654" y1="-1.7526" x2="1.3716" y2="-1.7526" width="0.1524" layer="39"/>
<wire x1="1.3716" y1="-1.7526" x2="1.3716" y2="-2.0066" width="0.1524" layer="39"/>
<wire x1="1.3716" y1="-2.0066" x2="-1.3716" y2="-2.0066" width="0.1524" layer="39"/>
<wire x1="-1.3716" y1="-2.0066" x2="-1.3716" y2="-1.7526" width="0.1524" layer="39"/>
<wire x1="-2.5654" y1="-1.7526" x2="-1.3716" y2="-1.7526" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-2.5654" y="-1.7628"/>
<vertex x="-2.5654" y="1.7628"/>
<vertex x="-1.3843" y="1.7628"/>
<vertex x="-1.3843" y="2.0066"/>
<vertex x="1.3843" y="2.0066"/>
<vertex x="1.3843" y="1.7628"/>
<vertex x="2.5654" y="1.7628"/>
<vertex x="2.5654" y="-1.7628"/>
<vertex x="1.3843" y="-1.7628"/>
<vertex x="1.3843" y="-2.0066"/>
<vertex x="-1.3843" y="-2.0066"/>
<vertex x="-1.3843" y="-1.7628"/>
</polygon>
<wire x1="-1.016" y1="-1.6256" x2="1.016" y2="-1.6256" width="0.1524" layer="21"/>
<wire x1="1.016" y1="1.6256" x2="-1.016" y2="1.6256" width="0.1524" layer="21"/>
<text x="-2.0828" y="1.4224" size="1.27" layer="21" ratio="6" rot="SR0">*</text>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="21-0058I-L">
<smd name="1" x="-1.143" y="0.95" dx="1.016" dy="0.508" layer="1"/>
<smd name="2" x="-1.143" y="0" dx="1.016" dy="0.508" layer="1"/>
<smd name="3" x="-1.143" y="-0.95" dx="1.016" dy="0.508" layer="1"/>
<smd name="4" x="1.143" y="-0.95" dx="1.016" dy="0.508" layer="1"/>
<smd name="5" x="1.143" y="0" dx="1.016" dy="0.508" layer="1"/>
<smd name="6" x="1.143" y="0.95" dx="1.016" dy="0.508" layer="1"/>
<wire x1="-0.8636" y1="0.6858" x2="-0.889" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="-0.889" y1="1.1938" x2="-1.4986" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="1.1938" x2="-1.4986" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="0.6858" x2="-0.8636" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-0.254" x2="-0.889" y2="0.254" width="0.1524" layer="51"/>
<wire x1="-0.889" y1="0.254" x2="-1.4986" y2="0.254" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="0.254" x2="-1.4986" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="-0.254" x2="-0.8636" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-1.1938" x2="-0.8636" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-0.6858" x2="-1.4986" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="-0.6858" x2="-1.4986" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="-1.4986" y1="-1.1938" x2="-0.8636" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="-0.6858" x2="0.889" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="0.889" y1="-1.1938" x2="1.4986" y2="-1.1938" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="-1.1938" x2="1.4986" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="-0.6858" x2="0.8636" y2="-0.6858" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="0.254" x2="0.8636" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="-0.254" x2="1.4986" y2="-0.254" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="-0.254" x2="1.4986" y2="0.254" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="0.254" x2="0.8636" y2="0.254" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="1.1938" x2="0.8636" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="0.6858" x2="1.4986" y2="0.6858" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="0.6858" x2="1.4986" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="1.4986" y1="1.1938" x2="0.8636" y2="1.1938" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="-1.4986" x2="0.8636" y2="-1.4986" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="-1.4986" x2="0.8636" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="0.8636" y1="1.4986" x2="0.3048" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="-0.3048" y1="1.4986" x2="-0.8636" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="-0.8636" y1="1.4986" x2="-0.8636" y2="-1.4986" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0.1524" layer="51" curve="-180"/>
<text x="-1.0668" y="0.1524" size="1.27" layer="51" ratio="6" rot="SR0">*</text>
<wire x1="-1.7526" y1="-1.2954" x2="-1.7526" y2="1.2954" width="0.1524" layer="39"/>
<wire x1="-1.7526" y1="1.2954" x2="-0.9652" y2="1.2954" width="0.1524" layer="39"/>
<wire x1="-0.9652" y1="1.2954" x2="-0.9652" y2="1.6002" width="0.1524" layer="39"/>
<wire x1="-0.9652" y1="1.6002" x2="0.9652" y2="1.6002" width="0.1524" layer="39"/>
<wire x1="0.9652" y1="1.6002" x2="0.9652" y2="1.2954" width="0.1524" layer="39"/>
<wire x1="1.7526" y1="1.2954" x2="0.9652" y2="1.2954" width="0.1524" layer="39"/>
<wire x1="1.7526" y1="1.2954" x2="1.7526" y2="-1.2954" width="0.1524" layer="39"/>
<wire x1="1.7526" y1="-1.2954" x2="0.9652" y2="-1.2954" width="0.1524" layer="39"/>
<wire x1="0.9652" y1="-1.2954" x2="0.9652" y2="-1.6002" width="0.1524" layer="39"/>
<wire x1="0.9652" y1="-1.6002" x2="-0.9652" y2="-1.6002" width="0.1524" layer="39"/>
<wire x1="-0.9652" y1="-1.6002" x2="-0.9652" y2="-1.2954" width="0.1524" layer="39"/>
<wire x1="-1.7526" y1="-1.2954" x2="-0.9652" y2="-1.2954" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-1.7526" y="-1.3056"/>
<vertex x="-1.7526" y="1.3056"/>
<vertex x="-0.9779" y="1.3056"/>
<vertex x="-0.9779" y="1.6002"/>
<vertex x="0.9779" y="1.6002"/>
<vertex x="0.9779" y="1.3056"/>
<vertex x="1.7526" y="1.3056"/>
<vertex x="1.7526" y="-1.3056"/>
<vertex x="0.9779" y="-1.3056"/>
<vertex x="0.9779" y="-1.6002"/>
<vertex x="-0.9779" y="-1.6002"/>
<vertex x="-0.9779" y="-1.3056"/>
</polygon>
<wire x1="-1.016" y1="-1.6256" x2="1.016" y2="-1.6256" width="0.1524" layer="21"/>
<wire x1="1.016" y1="1.6256" x2="-1.016" y2="1.6256" width="0.1524" layer="21"/>
<text x="-1.9812" y="1.3208" size="1.27" layer="21" ratio="6" rot="SR0">*</text>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
</packages>
<symbols>
<symbol name="MAX1921EUT18+">
<pin name="IN" x="2.54" y="0" length="middle" direction="in"/>
<pin name="AGND" x="2.54" y="-2.54" length="middle" direction="pwr"/>
<pin name="!SHDN" x="2.54" y="-5.08" length="middle" direction="pas"/>
<pin name="OUT" x="58.42" y="-5.08" length="middle" direction="out" rot="R180"/>
<pin name="PGND" x="58.42" y="-2.54" length="middle" direction="pwr" rot="R180"/>
<pin name="LX" x="58.42" y="0" length="middle" direction="pas" rot="R180"/>
<wire x1="7.62" y1="5.08" x2="7.62" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="7.62" y1="-10.16" x2="53.34" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="53.34" y1="-10.16" x2="53.34" y2="5.08" width="0.1524" layer="94"/>
<wire x1="53.34" y1="5.08" x2="7.62" y2="5.08" width="0.1524" layer="94"/>
<text x="25.7556" y="9.1186" size="2.0828" layer="95" ratio="6" rot="SR0">&gt;Name</text>
<text x="25.1206" y="6.5786" size="2.0828" layer="96" ratio="6" rot="SR0">&gt;Value</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="MAX1921EUT18+" prefix="U">
<gates>
<gate name="A" symbol="MAX1921EUT18+" x="0" y="0"/>
</gates>
<devices>
<device name="" package="21-0058I">
<connects>
<connect gate="A" pin="!SHDN" pad="3"/>
<connect gate="A" pin="AGND" pad="2"/>
<connect gate="A" pin="IN" pad="1"/>
<connect gate="A" pin="LX" pad="6"/>
<connect gate="A" pin="OUT" pad="4"/>
<connect gate="A" pin="PGND" pad="5"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="MAX1921EUT18+" constant="no"/>
<attribute name="VENDOR" value="Maxim Integrated Products" constant="no"/>
</technology>
</technologies>
</device>
<device name="21-0058I-M" package="21-0058I-M">
<connects>
<connect gate="A" pin="!SHDN" pad="3"/>
<connect gate="A" pin="AGND" pad="2"/>
<connect gate="A" pin="IN" pad="1"/>
<connect gate="A" pin="LX" pad="6"/>
<connect gate="A" pin="OUT" pad="4"/>
<connect gate="A" pin="PGND" pad="5"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="MAX1921EUT18+" constant="no"/>
<attribute name="VENDOR" value="Maxim Integrated Products" constant="no"/>
</technology>
</technologies>
</device>
<device name="21-0058I-L" package="21-0058I-L">
<connects>
<connect gate="A" pin="!SHDN" pad="3"/>
<connect gate="A" pin="AGND" pad="2"/>
<connect gate="A" pin="IN" pad="1"/>
<connect gate="A" pin="LX" pad="6"/>
<connect gate="A" pin="OUT" pad="4"/>
<connect gate="A" pin="PGND" pad="5"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="MAX1921EUT18+" constant="no"/>
<attribute name="VENDOR" value="Maxim Integrated Products" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="GLFR1608T4R7M-LR">
<packages>
<package name="INDC1608X95N">
<wire x1="-1.49" y1="0.74" x2="1.49" y2="0.74" width="0.05" layer="39"/>
<wire x1="1.49" y1="0.74" x2="1.49" y2="-0.74" width="0.05" layer="39"/>
<wire x1="1.49" y1="-0.74" x2="-1.49" y2="-0.74" width="0.05" layer="39"/>
<wire x1="-1.49" y1="-0.74" x2="-1.49" y2="0.74" width="0.05" layer="39"/>
<text x="-1.8713" y="1.019709375" size="0.800559375" layer="25">&gt;NAME</text>
<text x="-2.12611875" y="-1.02001875" size="0.8008" layer="27" align="top-left">&gt;VALUE</text>
<wire x1="-0.88" y1="-0.48" x2="-0.88" y2="0.48" width="0.127" layer="51"/>
<wire x1="-0.88" y1="0.48" x2="0.88" y2="0.48" width="0.127" layer="51"/>
<wire x1="0.88" y1="0.48" x2="0.88" y2="-0.48" width="0.127" layer="51"/>
<wire x1="0.88" y1="-0.48" x2="-0.88" y2="-0.48" width="0.127" layer="51"/>
<wire x1="-0.8" y1="0.665" x2="0.8" y2="0.665" width="0.127" layer="21"/>
<wire x1="-0.8" y1="-0.665" x2="0.8" y2="-0.665" width="0.127" layer="21"/>
<smd name="1" x="-0.785" y="0" dx="0.9" dy="0.97" layer="1" roundness="30"/>
<smd name="2" x="0.785" y="0" dx="0.9" dy="0.97" layer="1" roundness="30"/>
</package>
</packages>
<symbols>
<symbol name="GLFR1608T4R7M-LR">
<wire x1="-2.54" y1="0" x2="-1.27" y2="0" width="0.1524" layer="94" curve="-191.421"/>
<wire x1="-1.27" y1="0" x2="0" y2="0" width="0.1524" layer="94" curve="-191.421"/>
<wire x1="1.27" y1="0" x2="2.54" y2="0" width="0.1524" layer="94" curve="-191.421"/>
<wire x1="0" y1="0" x2="1.27" y2="0" width="0.1524" layer="94" curve="-191.421"/>
<text x="-5.08846875" y="1.90818125" size="1.780959375" layer="95">&gt;NAME</text>
<text x="-5.085440625" y="-2.54271875" size="1.779909375" layer="96">&gt;VALUE</text>
<pin name="2" x="7.62" y="0" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="1" x="-7.62" y="0" visible="pad" length="middle" direction="pas"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="GLFR1608T4R7M-LR" prefix="L">
<description>Inductor Power Chip Shielded Wirewound 4.7uH 20% 500mA 240mOhm DCR 0603 T/R</description>
<gates>
<gate name="G$1" symbol="GLFR1608T4R7M-LR" x="0" y="0"/>
</gates>
<devices>
<device name="" package="INDC1608X95N">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="DESCRIPTION" value=" GLFR Series 0603 4.7 uH ±20 % Tol. 0.24 Ohm DCR 110 mA Shielded Power Inductor "/>
<attribute name="DIGI-KEY_PART_NUMBER" value="445-3607-1-ND"/>
<attribute name="DIGI-KEY_PURCHASE_URL" value="https://www.digikey.co.uk/product-detail/en/tdk-corporation/GLFR1608T4R7M-LR/445-3607-1-ND/1856575?utm_source=snapeda&amp;utm_medium=aggregator&amp;utm_campaign=symbol"/>
<attribute name="MF" value="TDK"/>
<attribute name="MP" value="GLFR1608T4R7M-LR"/>
<attribute name="PACKAGE" value="0603 TDK"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="0402 footprint ">
<packages>
<package name="RES0402_CRG_TYCO">
<smd name="1" x="-0.5461" y="0" dx="0.7112" dy="0.5588" layer="1"/>
<smd name="2" x="0.5461" y="0" dx="0.7112" dy="0.5588" layer="1"/>
<wire x1="-1.1684" y1="-0.5334" x2="-1.1684" y2="0.5334" width="0.1524" layer="39"/>
<wire x1="-1.1684" y1="0.5334" x2="1.1684" y2="0.5334" width="0.1524" layer="39"/>
<wire x1="1.1684" y1="0.5334" x2="1.1684" y2="-0.5334" width="0.1524" layer="39"/>
<wire x1="1.1684" y1="-0.5334" x2="-1.1684" y2="-0.5334" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-1.1557" y="-0.5334"/>
<vertex x="-1.1557" y="0.5334"/>
<vertex x="1.1557" y="0.5334"/>
<vertex x="1.1557" y="-0.5334"/>
</polygon>
<wire x1="-0.2032" y1="-0.2794" x2="-0.2032" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.2032" y1="0.2794" x2="-0.5588" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5588" y1="-0.2794" x2="-0.2032" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="0.2794" x2="0.2032" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.2032" y1="-0.2794" x2="0.5588" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5588" y1="-0.2794" x2="0.5334" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="0.5334" y1="0.2794" x2="0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.2032" y1="-0.2794" x2="0.2032" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5588" y1="-0.2794" x2="0.5588" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="0.5588" y1="0.2794" x2="-0.2032" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5588" y1="0.2794" x2="-0.5588" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<polygon width="0.1524" layer="41">
<vertex x="-0.1397" y="0.2794"/>
<vertex x="0.1397" y="0.2794"/>
<vertex x="0.1397" y="-0.2794"/>
<vertex x="-0.1397" y="-0.2794"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1397" y="0.2794"/>
<vertex x="0.1397" y="0.2794"/>
<vertex x="0.1397" y="-0.2794"/>
<vertex x="-0.1397" y="-0.2794"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1397" y="0.2286"/>
<vertex x="0.1397" y="0.2286"/>
<vertex x="0.1397" y="-0.2286"/>
<vertex x="-0.1397" y="-0.2286"/>
</polygon>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="RES0402_CRG_TYCO-M">
<smd name="1" x="-0.6477" y="0" dx="0.9144" dy="0.6604" layer="1"/>
<smd name="2" x="0.6477" y="0" dx="0.9144" dy="0.6604" layer="1"/>
<wire x1="-1.6256" y1="-0.8382" x2="-1.6256" y2="0.8382" width="0.1524" layer="39"/>
<wire x1="-1.6256" y1="0.8382" x2="1.6256" y2="0.8382" width="0.1524" layer="39"/>
<wire x1="1.6256" y1="0.8382" x2="1.6256" y2="-0.8382" width="0.1524" layer="39"/>
<wire x1="1.6256" y1="-0.8382" x2="-1.6256" y2="-0.8382" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-1.6129" y="-0.8382"/>
<vertex x="-1.6129" y="0.8382"/>
<vertex x="1.6129" y="0.8382"/>
<vertex x="1.6129" y="-0.8382"/>
</polygon>
<wire x1="-0.2032" y1="-0.2794" x2="-0.2032" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.2032" y1="0.2794" x2="-0.5588" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5588" y1="-0.2794" x2="-0.2032" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="0.2794" x2="0.2032" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.2032" y1="-0.2794" x2="0.5588" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5588" y1="-0.2794" x2="0.5334" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="0.5334" y1="0.2794" x2="0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.2032" y1="-0.2794" x2="0.2032" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5588" y1="-0.2794" x2="0.5588" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="0.5588" y1="0.2794" x2="-0.2032" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5588" y1="0.2794" x2="-0.5588" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<polygon width="0.1524" layer="41">
<vertex x="-0.1397" y="0.2794"/>
<vertex x="0.1397" y="0.2794"/>
<vertex x="0.1397" y="-0.2794"/>
<vertex x="-0.1397" y="-0.2794"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1397" y="0.2794"/>
<vertex x="0.1397" y="0.2794"/>
<vertex x="0.1397" y="-0.2794"/>
<vertex x="-0.1397" y="-0.2794"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1397" y="0.2286"/>
<vertex x="0.1397" y="0.2286"/>
<vertex x="0.1397" y="-0.2286"/>
<vertex x="-0.1397" y="-0.2286"/>
</polygon>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="RES0402_CRG_TYCO-L">
<smd name="1" x="-0.4445" y="0" dx="0.508" dy="0.4572" layer="1"/>
<smd name="2" x="0.4445" y="0" dx="0.508" dy="0.4572" layer="1"/>
<wire x1="-0.8128" y1="-0.3302" x2="-0.8128" y2="0.3302" width="0.1524" layer="39"/>
<wire x1="-0.8128" y1="0.3302" x2="0.8128" y2="0.3302" width="0.1524" layer="39"/>
<wire x1="0.8128" y1="0.3302" x2="0.8128" y2="-0.3302" width="0.1524" layer="39"/>
<wire x1="0.8128" y1="-0.3302" x2="-0.8128" y2="-0.3302" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-0.8001" y="-0.3302"/>
<vertex x="-0.8001" y="0.3302"/>
<vertex x="0.8001" y="0.3302"/>
<vertex x="0.8001" y="-0.3302"/>
</polygon>
<wire x1="-0.2032" y1="-0.2794" x2="-0.2032" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.2032" y1="0.2794" x2="-0.5588" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5588" y1="-0.2794" x2="-0.2032" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="0.2794" x2="0.2032" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.2032" y1="-0.2794" x2="0.5588" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5588" y1="-0.2794" x2="0.5334" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="0.5334" y1="0.2794" x2="0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.2032" y1="-0.2794" x2="0.2032" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5588" y1="-0.2794" x2="0.5588" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="0.5588" y1="0.2794" x2="-0.2032" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5588" y1="0.2794" x2="-0.5588" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<polygon width="0.1524" layer="41">
<vertex x="-0.1397" y="0.2794"/>
<vertex x="0.1397" y="0.2794"/>
<vertex x="0.1397" y="-0.2794"/>
<vertex x="-0.1397" y="-0.2794"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1397" y="0.2794"/>
<vertex x="0.1397" y="0.2794"/>
<vertex x="0.1397" y="-0.2794"/>
<vertex x="-0.1397" y="-0.2794"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1397" y="0.2286"/>
<vertex x="0.1397" y="0.2286"/>
<vertex x="0.1397" y="-0.2286"/>
<vertex x="-0.1397" y="-0.2286"/>
</polygon>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
</packages>
<symbols>
<symbol name="RES">
<pin name="2" x="0" y="0" visible="pin" length="short" direction="pas" swaplevel="1"/>
<pin name="1" x="12.7" y="0" visible="off" length="short" direction="pas" rot="R180"/>
<wire x1="3.175" y1="1.27" x2="4.445" y2="-1.27" width="0.2032" layer="94"/>
<wire x1="4.445" y1="-1.27" x2="5.715" y2="1.27" width="0.2032" layer="94"/>
<wire x1="5.715" y1="1.27" x2="6.985" y2="-1.27" width="0.2032" layer="94"/>
<wire x1="6.985" y1="-1.27" x2="8.255" y2="1.27" width="0.2032" layer="94"/>
<wire x1="8.255" y1="1.27" x2="9.525" y2="-1.27" width="0.2032" layer="94"/>
<wire x1="2.54" y1="0" x2="3.175" y2="1.27" width="0.2032" layer="94"/>
<wire x1="9.525" y1="-1.27" x2="10.16" y2="0" width="0.2032" layer="94"/>
<text x="-2.6162" y="-5.5372" size="3.4798" layer="96" ratio="10" rot="SR0">&gt;Value</text>
<text x="-2.1844" y="2.0828" size="3.4798" layer="95" ratio="10" rot="SR0">&gt;Name</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="CRG0402J1K0/10" prefix="R">
<gates>
<gate name="A" symbol="RES" x="0" y="0" swaplevel="1"/>
</gates>
<devices>
<device name="" package="RES0402_CRG_TYCO">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="CRG0402J1K010" constant="no"/>
<attribute name="VENDOR" value="TE Connectivity" constant="no"/>
</technology>
</technologies>
</device>
<device name="RES0402_CRG_TYCO-M" package="RES0402_CRG_TYCO-M">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="CRG0402J1K010" constant="no"/>
<attribute name="VENDOR" value="TE Connectivity" constant="no"/>
</technology>
</technologies>
</device>
<device name="RES0402_CRG_TYCO-L" package="RES0402_CRG_TYCO-L">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="CRG0402J1K010" constant="no"/>
<attribute name="VENDOR" value="TE Connectivity" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="0402 footprint capacitor">
<packages>
<package name="CAP_CHIP2_1X0P5">
<smd name="1" x="-0.5278" y="0" dx="0.7056" dy="0.55" layer="1"/>
<smd name="2" x="0.5278" y="0" dx="0.7056" dy="0.55" layer="1"/>
<wire x1="-1.143" y1="-0.5334" x2="-1.143" y2="0.5334" width="0.1524" layer="39"/>
<wire x1="-1.143" y1="0.5334" x2="1.143" y2="0.5334" width="0.1524" layer="39"/>
<wire x1="1.143" y1="0.5334" x2="1.143" y2="-0.5334" width="0.1524" layer="39"/>
<wire x1="1.143" y1="-0.5334" x2="-1.143" y2="-0.5334" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-1.1346" y="-0.529"/>
<vertex x="-1.1346" y="0.529"/>
<vertex x="1.1346" y="0.529"/>
<vertex x="1.1346" y="-0.529"/>
</polygon>
<wire x1="-1.651" y1="0" x2="-1.8034" y2="0" width="0.1524" layer="21" curve="-180"/>
<wire x1="-1.8034" y1="0" x2="-1.651" y2="0" width="0.1524" layer="21" curve="-180"/>
<wire x1="-0.1778" y1="-0.2794" x2="-0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.1778" y1="0.2794" x2="-0.5334" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5334" y1="-0.2794" x2="-0.1778" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="0.2794" x2="0.1778" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="-0.2794" x2="0.5334" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5334" y1="0.2794" x2="0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.1778" y1="-0.2794" x2="0.1778" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5334" y1="-0.2794" x2="0.5334" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="0.2794" x2="-0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5334" y1="0.2794" x2="-0.5334" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="-0.3302" y1="0" x2="-0.4826" y2="0" width="0" layer="51" curve="-180"/>
<wire x1="-0.4826" y1="0" x2="-0.3302" y2="0" width="0" layer="51" curve="-180"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<polygon width="0.1524" layer="41">
<vertex x="-0.1242" y="0.275"/>
<vertex x="0.1242" y="0.275"/>
<vertex x="0.1242" y="-0.275"/>
<vertex x="-0.1242" y="-0.275"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1242" y="0.275"/>
<vertex x="0.1242" y="0.275"/>
<vertex x="0.1242" y="-0.275"/>
<vertex x="-0.1242" y="-0.275"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1242" y="0.2242"/>
<vertex x="0.1242" y="0.2242"/>
<vertex x="0.1242" y="-0.2242"/>
<vertex x="-0.1242" y="-0.2242"/>
</polygon>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="CAP_CHIP2_1X0P5-M">
<smd name="1" x="-0.6294" y="0" dx="0.9088" dy="0.6516" layer="1"/>
<smd name="2" x="0.6294" y="0" dx="0.9088" dy="0.6516" layer="1"/>
<wire x1="-1.6002" y1="-0.8382" x2="-1.6002" y2="0.8382" width="0.1524" layer="39"/>
<wire x1="-1.6002" y1="0.8382" x2="1.6002" y2="0.8382" width="0.1524" layer="39"/>
<wire x1="1.6002" y1="0.8382" x2="1.6002" y2="-0.8382" width="0.1524" layer="39"/>
<wire x1="1.6002" y1="-0.8382" x2="-1.6002" y2="-0.8382" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-1.5918" y="-0.8338"/>
<vertex x="-1.5918" y="0.8338"/>
<vertex x="1.5918" y="0.8338"/>
<vertex x="1.5918" y="-0.8338"/>
</polygon>
<wire x1="-1.8542" y1="0" x2="-2.0066" y2="0" width="0.1524" layer="21" curve="-180"/>
<wire x1="-2.0066" y1="0" x2="-1.8542" y2="0" width="0.1524" layer="21" curve="-180"/>
<wire x1="-0.1778" y1="-0.2794" x2="-0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.1778" y1="0.2794" x2="-0.5334" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5334" y1="-0.2794" x2="-0.1778" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="0.2794" x2="0.1778" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="-0.2794" x2="0.5334" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5334" y1="0.2794" x2="0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.1778" y1="-0.2794" x2="0.1778" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5334" y1="-0.2794" x2="0.5334" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="0.2794" x2="-0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5334" y1="0.2794" x2="-0.5334" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="-0.4318" y1="0" x2="-0.5842" y2="0" width="0" layer="51" curve="-180"/>
<wire x1="-0.5842" y1="0" x2="-0.4318" y2="0" width="0" layer="51" curve="-180"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<polygon width="0.1524" layer="41">
<vertex x="-0.1242" y="0.275"/>
<vertex x="0.1242" y="0.275"/>
<vertex x="0.1242" y="-0.275"/>
<vertex x="-0.1242" y="-0.275"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1242" y="0.275"/>
<vertex x="0.1242" y="0.275"/>
<vertex x="0.1242" y="-0.275"/>
<vertex x="-0.1242" y="-0.275"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1242" y="0.2242"/>
<vertex x="0.1242" y="0.2242"/>
<vertex x="0.1242" y="-0.2242"/>
<vertex x="-0.1242" y="-0.2242"/>
</polygon>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
<package name="CAP_CHIP2_1X0P5-L">
<smd name="1" x="-0.4262" y="0" dx="0.5024" dy="0.4484" layer="1"/>
<smd name="2" x="0.4262" y="0" dx="0.5024" dy="0.4484" layer="1"/>
<wire x1="-0.7874" y1="-0.3302" x2="-0.7874" y2="0.3302" width="0.1524" layer="39"/>
<wire x1="-0.7874" y1="0.3302" x2="0.7874" y2="0.3302" width="0.1524" layer="39"/>
<wire x1="0.7874" y1="0.3302" x2="0.7874" y2="-0.3302" width="0.1524" layer="39"/>
<wire x1="0.7874" y1="-0.3302" x2="-0.7874" y2="-0.3302" width="0.1524" layer="39"/>
<polygon width="0.1524" layer="39">
<vertex x="-0.779" y="-0.3258"/>
<vertex x="-0.779" y="0.3258"/>
<vertex x="0.779" y="0.3258"/>
<vertex x="0.779" y="-0.3258"/>
</polygon>
<wire x1="-1.4478" y1="0" x2="-1.6002" y2="0" width="0.1524" layer="21" curve="-180"/>
<wire x1="-1.6002" y1="0" x2="-1.4478" y2="0" width="0.1524" layer="21" curve="-180"/>
<wire x1="-0.1778" y1="-0.2794" x2="-0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.1778" y1="0.2794" x2="-0.5334" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5334" y1="-0.2794" x2="-0.1778" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="0.2794" x2="0.1778" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="-0.2794" x2="0.5334" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5334" y1="0.2794" x2="0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.1778" y1="-0.2794" x2="0.1778" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="0.5334" y1="-0.2794" x2="0.5334" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="0.1778" y1="0.2794" x2="-0.1778" y2="0.2794" width="0.1524" layer="51"/>
<wire x1="-0.5334" y1="0.2794" x2="-0.5334" y2="-0.2794" width="0.1524" layer="51"/>
<wire x1="-0.2286" y1="0" x2="-0.381" y2="0" width="0" layer="51" curve="-180"/>
<wire x1="-0.381" y1="0" x2="-0.2286" y2="0" width="0" layer="51" curve="-180"/>
<wire x1="-0.254" y1="0" x2="0.254" y2="0" width="0.1524" layer="23"/>
<wire x1="0" y1="-0.254" x2="0" y2="0.254" width="0.1524" layer="23"/>
<polygon width="0.1524" layer="41">
<vertex x="-0.1242" y="0.275"/>
<vertex x="0.1242" y="0.275"/>
<vertex x="0.1242" y="-0.275"/>
<vertex x="-0.1242" y="-0.275"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1242" y="0.275"/>
<vertex x="0.1242" y="0.275"/>
<vertex x="0.1242" y="-0.275"/>
<vertex x="-0.1242" y="-0.275"/>
</polygon>
<polygon width="0.1524" layer="41">
<vertex x="-0.1242" y="0.2242"/>
<vertex x="0.1242" y="0.2242"/>
<vertex x="0.1242" y="-0.2242"/>
<vertex x="-0.1242" y="-0.2242"/>
</polygon>
<text x="-3.2766" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
</package>
</packages>
<symbols>
<symbol name="CAPH">
<pin name="2" x="7.62" y="0" visible="off" length="short" direction="pas" swaplevel="1" rot="R180"/>
<pin name="1" x="0" y="0" visible="off" length="short" direction="pas" swaplevel="1"/>
<wire x1="3.4798" y1="-1.905" x2="3.4798" y2="0" width="0.2032" layer="94"/>
<wire x1="3.4798" y1="0" x2="3.4798" y2="1.905" width="0.2032" layer="94"/>
<wire x1="4.1148" y1="-1.905" x2="4.1148" y2="0" width="0.2032" layer="94"/>
<wire x1="4.1148" y1="0" x2="4.1148" y2="1.905" width="0.2032" layer="94"/>
<wire x1="4.1148" y1="0" x2="5.08" y2="0" width="0.2032" layer="94"/>
<wire x1="2.54" y1="0" x2="3.4798" y2="0" width="0.2032" layer="94"/>
<text x="-5.1562" y="-5.5372" size="3.4798" layer="96" ratio="10" rot="SR0">&gt;Value</text>
<text x="-4.0894" y="2.0828" size="3.4798" layer="95" ratio="10" rot="SR0">&gt;Name</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="GRM155R61A105KE15D" prefix="C">
<gates>
<gate name="A" symbol="CAPH" x="0" y="0" swaplevel="1"/>
</gates>
<devices>
<device name="" package="CAP_CHIP2_1X0P5">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="GRM155R61A105KE15D" constant="no"/>
<attribute name="VENDOR" value="Murata" constant="no"/>
</technology>
</technologies>
</device>
<device name="CAP_CHIP2_1X0P5-M" package="CAP_CHIP2_1X0P5-M">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="GRM155R61A105KE15D" constant="no"/>
<attribute name="VENDOR" value="Murata" constant="no"/>
</technology>
</technologies>
</device>
<device name="CAP_CHIP2_1X0P5-L" package="CAP_CHIP2_1X0P5-L">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="MANUFACTURER_PART_NUMBER" value="GRM155R61A105KE15D" constant="no"/>
<attribute name="VENDOR" value="Murata" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply1" urn="urn:adsk.eagle:library:371">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
 GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
 Please keep in mind, that these devices are necessary for the
 automatic wiring of the supply signals.&lt;p&gt;
 The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
 In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
 &lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="V+" urn="urn:adsk.eagle:symbol:26939/1" library_version="1">
<wire x1="0.889" y1="-1.27" x2="0" y2="0.127" width="0.254" layer="94"/>
<wire x1="0" y1="0.127" x2="-0.889" y2="-1.27" width="0.254" layer="94"/>
<wire x1="-0.889" y1="-1.27" x2="0.889" y2="-1.27" width="0.254" layer="94"/>
<text x="-2.54" y="-2.54" size="1.778" layer="96" rot="R90">&gt;VALUE</text>
<pin name="V+" x="0" y="-2.54" visible="off" length="short" direction="sup" rot="R90"/>
</symbol>
<symbol name="GND" urn="urn:adsk.eagle:symbol:26925/1" library_version="1">
<wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94"/>
<text x="-2.54" y="-2.54" size="1.778" layer="96">&gt;VALUE</text>
<pin name="GND" x="0" y="2.54" visible="off" length="short" direction="sup" rot="R270"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="V+" urn="urn:adsk.eagle:component:26966/1" prefix="P+" library_version="1">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="V+" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="GND" urn="urn:adsk.eagle:component:26954/1" prefix="GND" library_version="1">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="GND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="pinhead" urn="urn:adsk.eagle:library:325">
<description>&lt;b&gt;Pin Header Connectors&lt;/b&gt;&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="1X01" urn="urn:adsk.eagle:footprint:22382/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-0.635" y1="1.27" x2="0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="1.27" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-0.635" x2="0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="1.27" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-0.635" x2="-0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="-1.27" x2="-0.635" y2="-1.27" width="0.1524" layer="21"/>
<pad name="1" x="0" y="0" drill="1.016" shape="octagon"/>
<text x="-1.3462" y="1.8288" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-1.27" y="-3.175" size="1.27" layer="27">&gt;VALUE</text>
<rectangle x1="-0.254" y1="-0.254" x2="0.254" y2="0.254" layer="51"/>
</package>
</packages>
<packages3d>
<package3d name="1X01" urn="urn:adsk.eagle:package:22485/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X01"/>
</packageinstances>
</package3d>
</packages3d>
<symbols>
<symbol name="PINHD1" urn="urn:adsk.eagle:symbol:22381/1" library_version="3">
<wire x1="-6.35" y1="-2.54" x2="1.27" y2="-2.54" width="0.4064" layer="94"/>
<wire x1="1.27" y1="-2.54" x2="1.27" y2="2.54" width="0.4064" layer="94"/>
<wire x1="1.27" y1="2.54" x2="-6.35" y2="2.54" width="0.4064" layer="94"/>
<wire x1="-6.35" y1="2.54" x2="-6.35" y2="-2.54" width="0.4064" layer="94"/>
<text x="-6.35" y="3.175" size="1.778" layer="95">&gt;NAME</text>
<text x="-6.35" y="-5.08" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-2.54" y="0" visible="pad" length="short" direction="pas" function="dot"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="PINHD-1X1" urn="urn:adsk.eagle:component:22540/2" prefix="JP" uservalue="yes" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<gates>
<gate name="G$1" symbol="PINHD1" x="0" y="0"/>
</gates>
<devices>
<device name="" package="1X01">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22485/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U1" library="MAX30102EFD+" deviceset="MAX30102EFD+" device=""/>
<part name="U2" library="MAX14595ETA+" deviceset="MAX14595ETA+" device=""/>
<part name="U3" library="MAX1921EUT18+" deviceset="MAX1921EUT18+" device=""/>
<part name="L1" library="GLFR1608T4R7M-LR" deviceset="GLFR1608T4R7M-LR" device=""/>
<part name="R1" library="0402 footprint " deviceset="CRG0402J1K0/10" device="" value="4.7K"/>
<part name="R2" library="0402 footprint " deviceset="CRG0402J1K0/10" device="" value="4.7K"/>
<part name="R3" library="0402 footprint " deviceset="CRG0402J1K0/10" device="" value="4.7K"/>
<part name="R4" library="0402 footprint " deviceset="CRG0402J1K0/10" device="" value="4.7K"/>
<part name="R5" library="0402 footprint " deviceset="CRG0402J1K0/10" device="" value="4.7K"/>
<part name="R6" library="0402 footprint " deviceset="CRG0402J1K0/10" device="" value="4.75K"/>
<part name="C1" library="0402 footprint capacitor" deviceset="GRM155R61A105KE15D" device="" value="1u"/>
<part name="C2" library="0402 footprint capacitor" deviceset="GRM155R61A105KE15D" device="" value="1u"/>
<part name="C3" library="0402 footprint capacitor" deviceset="GRM155R61A105KE15D" device="" value="4.7u"/>
<part name="C4" library="0402 footprint capacitor" deviceset="GRM155R61A105KE15D" device="" value="4.7u"/>
<part name="C5" library="0402 footprint capacitor" deviceset="GRM155R61A105KE15D" device="" value="5600p"/>
<part name="C6" library="0402 footprint capacitor" deviceset="GRM155R61A105KE15D" device="" value="0.1u"/>
<part name="C7" library="0402 footprint capacitor" deviceset="GRM155R61A105KE15D" device="" value="0.1u"/>
<part name="P+1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="V+" device=""/>
<part name="GND1" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND2" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="P+2" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="V+" device=""/>
<part name="GND3" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND4" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND5" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND6" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="P+3" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="V+" device=""/>
<part name="P+4" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="V+" device=""/>
<part name="P+5" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="V+" device=""/>
<part name="GND7" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND8" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="P+6" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="V+" device=""/>
<part name="P+7" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="V+" device=""/>
<part name="GND9" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND10" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="GND11" library="supply1" library_urn="urn:adsk.eagle:library:371" deviceset="GND" device=""/>
<part name="INT" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X1" device="" package3d_urn="urn:adsk.eagle:package:22485/2" value="INT"/>
<part name="V+" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X1" device="" package3d_urn="urn:adsk.eagle:package:22485/2" value="V+"/>
<part name="SCL" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X1" device="" package3d_urn="urn:adsk.eagle:package:22485/2" value="SCL"/>
<part name="SDA" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X1" device="" package3d_urn="urn:adsk.eagle:package:22485/2" value="SDA"/>
<part name="GND" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X1" device="" package3d_urn="urn:adsk.eagle:package:22485/2" value="GND"/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U1" gate="A" x="-5.08" y="66.04" smashed="yes">
<attribute name="NAME" x="23.2156" y="85.3186" size="2.0828" layer="95" ratio="6" rot="SR0"/>
<attribute name="VALUE" x="22.5806" y="80.2386" size="2.0828" layer="96" ratio="6" rot="SR0"/>
</instance>
<instance part="U2" gate="A" x="-55.88" y="53.34" smashed="yes" rot="R180">
<attribute name="NAME" x="-84.1756" y="44.2214" size="2.0828" layer="95" ratio="6" rot="SR180"/>
<attribute name="VALUE" x="-83.5406" y="46.7614" size="2.0828" layer="96" ratio="6" rot="SR180"/>
</instance>
<instance part="U3" gate="A" x="-63.5" y="-5.08" smashed="yes">
<attribute name="NAME" x="-42.8244" y="4.0386" size="2.0828" layer="95" ratio="6" rot="SR0"/>
<attribute name="VALUE" x="-48.5394" y="1.4986" size="2.0828" layer="96" ratio="6" rot="SR0"/>
</instance>
<instance part="L1" gate="G$1" x="27.94" y="-5.08" smashed="yes">
<attribute name="NAME" x="22.85153125" y="-3.17181875" size="1.780959375" layer="95"/>
<attribute name="VALUE" x="20.314559375" y="-7.62271875" size="1.779909375" layer="96"/>
</instance>
<instance part="R1" gate="A" x="-35.56" y="48.26" smashed="yes">
<attribute name="VALUE" x="-33.0962" y="42.7228" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="-32.6644" y="50.3428" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="R2" gate="A" x="-35.56" y="68.58" smashed="yes">
<attribute name="VALUE" x="-38.1762" y="63.0428" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="-37.7444" y="70.6628" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="R3" gate="A" x="68.58" y="78.74" smashed="yes">
<attribute name="VALUE" x="68.5038" y="73.2028" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="68.9356" y="80.8228" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="R4" gate="A" x="-144.78" y="68.58" smashed="yes">
<attribute name="VALUE" x="-147.3962" y="63.0428" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="-146.9644" y="70.6628" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="R5" gate="A" x="-144.78" y="45.72" smashed="yes">
<attribute name="VALUE" x="-147.3962" y="40.1828" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="-146.9644" y="47.8028" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="R6" gate="A" x="5.08" y="-10.16" smashed="yes">
<attribute name="VALUE" x="7.5438" y="-15.6972" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="7.9756" y="-8.0772" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="C1" gate="A" x="73.66" y="55.88" smashed="yes">
<attribute name="VALUE" x="73.5838" y="52.8828" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="74.6506" y="57.9628" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="C2" gate="A" x="78.74" y="38.1" smashed="yes" rot="R270">
<attribute name="VALUE" x="80.8228" y="38.1762" size="3.4798" layer="96" ratio="10" rot="SR270"/>
<attribute name="NAME" x="73.2028" y="37.1094" size="3.4798" layer="95" ratio="10" rot="SR270"/>
</instance>
<instance part="C3" gate="A" x="-71.12" y="0" smashed="yes">
<attribute name="VALUE" x="-71.1962" y="-2.9972" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="-70.1294" y="2.0828" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="C4" gate="A" x="38.1" y="-5.08" smashed="yes">
<attribute name="VALUE" x="32.9438" y="-10.6172" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="34.0106" y="-2.9972" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="C5" gate="A" x="12.7" y="-20.32" smashed="yes">
<attribute name="VALUE" x="10.0838" y="-25.8572" size="3.4798" layer="96" ratio="10" rot="SR0"/>
<attribute name="NAME" x="11.1506" y="-18.2372" size="3.4798" layer="95" ratio="10" rot="SR0"/>
</instance>
<instance part="C6" gate="A" x="-111.76" y="40.64" smashed="yes" rot="R270">
<attribute name="VALUE" x="-109.6772" y="40.7162" size="3.4798" layer="96" ratio="10" rot="SR270"/>
<attribute name="NAME" x="-117.2972" y="39.6494" size="3.4798" layer="95" ratio="10" rot="SR270"/>
</instance>
<instance part="C7" gate="A" x="-66.04" y="40.64" smashed="yes" rot="R270">
<attribute name="VALUE" x="-63.9572" y="38.1762" size="3.4798" layer="96" ratio="10" rot="SR270"/>
<attribute name="NAME" x="-71.5772" y="37.1094" size="3.4798" layer="95" ratio="10" rot="SR270"/>
</instance>
<instance part="P+1" gate="1" x="83.82" y="83.82" smashed="yes">
<attribute name="VALUE" x="86.36" y="86.36" size="1.778" layer="96" rot="R180"/>
</instance>
<instance part="GND1" gate="1" x="63.5" y="55.88" smashed="yes" rot="R90">
<attribute name="VALUE" x="66.04" y="53.34" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="GND2" gate="1" x="86.36" y="55.88" smashed="yes" rot="R90">
<attribute name="VALUE" x="88.9" y="53.34" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="P+2" gate="1" x="78.74" y="45.72" smashed="yes" rot="R270">
<attribute name="VALUE" x="78.74" y="45.72" size="1.778" layer="96"/>
</instance>
<instance part="GND3" gate="1" x="78.74" y="25.4" smashed="yes">
<attribute name="VALUE" x="76.2" y="22.86" size="1.778" layer="96"/>
</instance>
<instance part="GND4" gate="1" x="-10.16" y="50.8" smashed="yes" rot="R270">
<attribute name="VALUE" x="-12.7" y="53.34" size="1.778" layer="96" rot="R270"/>
</instance>
<instance part="GND5" gate="1" x="-66.04" y="27.94" smashed="yes">
<attribute name="VALUE" x="-68.58" y="25.4" size="1.778" layer="96"/>
</instance>
<instance part="GND6" gate="1" x="-121.92" y="66.04" smashed="yes" rot="R180">
<attribute name="VALUE" x="-119.38" y="68.58" size="1.778" layer="96" rot="R180"/>
</instance>
<instance part="P+3" gate="1" x="-149.86" y="71.12" smashed="yes">
<attribute name="VALUE" x="-147.32" y="73.66" size="1.778" layer="96" rot="R180"/>
</instance>
<instance part="P+4" gate="1" x="-149.86" y="43.18" smashed="yes" rot="R180">
<attribute name="VALUE" x="-152.4" y="40.64" size="1.778" layer="96"/>
</instance>
<instance part="P+5" gate="1" x="-119.38" y="35.56" smashed="yes" rot="R180">
<attribute name="VALUE" x="-121.92" y="33.02" size="1.778" layer="96"/>
</instance>
<instance part="GND7" gate="1" x="-111.76" y="27.94" smashed="yes">
<attribute name="VALUE" x="-114.3" y="25.4" size="1.778" layer="96"/>
</instance>
<instance part="GND8" gate="1" x="-76.2" y="0" smashed="yes" rot="R270">
<attribute name="VALUE" x="-78.74" y="2.54" size="1.778" layer="96" rot="R270"/>
</instance>
<instance part="P+6" gate="1" x="-60.96" y="10.16" smashed="yes">
<attribute name="VALUE" x="-58.42" y="12.7" size="1.778" layer="96" rot="R180"/>
</instance>
<instance part="P+7" gate="1" x="-60.96" y="-17.78" smashed="yes" rot="R180">
<attribute name="VALUE" x="-63.5" y="-20.32" size="1.778" layer="96"/>
</instance>
<instance part="GND9" gate="1" x="-66.04" y="-7.62" smashed="yes" rot="R270">
<attribute name="VALUE" x="-68.58" y="-5.08" size="1.778" layer="96" rot="R270"/>
</instance>
<instance part="GND10" gate="1" x="0" y="-7.62" smashed="yes" rot="R90">
<attribute name="VALUE" x="2.54" y="-10.16" size="1.778" layer="96" rot="R90"/>
</instance>
<instance part="GND11" gate="1" x="48.26" y="-2.54" smashed="yes" rot="R180">
<attribute name="VALUE" x="50.8" y="0" size="1.778" layer="96" rot="R180"/>
</instance>
<instance part="INT" gate="G$1" x="-137.16" y="5.08" smashed="yes">
<attribute name="NAME" x="-143.51" y="8.255" size="1.778" layer="95"/>
<attribute name="VALUE" x="-143.51" y="0" size="1.778" layer="96"/>
</instance>
<instance part="V+" gate="G$1" x="-121.92" y="5.08" smashed="yes">
<attribute name="NAME" x="-128.27" y="8.255" size="1.778" layer="95"/>
<attribute name="VALUE" x="-128.27" y="0" size="1.778" layer="96"/>
</instance>
<instance part="SCL" gate="G$1" x="-137.16" y="-5.08" smashed="yes">
<attribute name="NAME" x="-143.51" y="-1.905" size="1.778" layer="95"/>
<attribute name="VALUE" x="-143.51" y="-10.16" size="1.778" layer="96"/>
</instance>
<instance part="SDA" gate="G$1" x="-121.92" y="-5.08" smashed="yes">
<attribute name="NAME" x="-128.27" y="-1.905" size="1.778" layer="95"/>
<attribute name="VALUE" x="-128.27" y="-10.16" size="1.778" layer="96"/>
</instance>
<instance part="GND" gate="G$1" x="-129.54" y="-17.78" smashed="yes">
<attribute name="NAME" x="-135.89" y="-14.605" size="1.778" layer="95"/>
<attribute name="VALUE" x="-135.89" y="-22.86" size="1.778" layer="96"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="N$1" class="0">
<segment>
<pinref part="U1" gate="A" pin="SCL"/>
<wire x1="-2.54" y1="60.96" x2="-20.32" y2="60.96" width="0.1524" layer="91"/>
<wire x1="-20.32" y1="60.96" x2="-20.32" y2="68.58" width="0.1524" layer="91"/>
<pinref part="R2" gate="A" pin="1"/>
<wire x1="-20.32" y1="68.58" x2="-22.86" y2="68.58" width="0.1524" layer="91"/>
<wire x1="-20.32" y1="60.96" x2="-48.26" y2="60.96" width="0.1524" layer="91"/>
<junction x="-20.32" y="60.96"/>
<wire x1="-48.26" y1="60.96" x2="-48.26" y2="55.88" width="0.1524" layer="91"/>
<pinref part="U2" gate="A" pin="IOVL2"/>
<wire x1="-48.26" y1="55.88" x2="-58.42" y2="55.88" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<pinref part="U1" gate="A" pin="SDA"/>
<wire x1="-2.54" y1="55.88" x2="-20.32" y2="55.88" width="0.1524" layer="91"/>
<wire x1="-20.32" y1="55.88" x2="-20.32" y2="48.26" width="0.1524" layer="91"/>
<pinref part="R1" gate="A" pin="1"/>
<wire x1="-20.32" y1="48.26" x2="-22.86" y2="48.26" width="0.1524" layer="91"/>
<wire x1="-20.32" y1="55.88" x2="-45.72" y2="55.88" width="0.1524" layer="91"/>
<junction x="-20.32" y="55.88"/>
<wire x1="-45.72" y1="55.88" x2="-45.72" y2="58.42" width="0.1524" layer="91"/>
<pinref part="U2" gate="A" pin="IOVL1"/>
<wire x1="-45.72" y1="58.42" x2="-58.42" y2="58.42" width="0.1524" layer="91"/>
</segment>
</net>
<net name="INT" class="0">
<segment>
<pinref part="U1" gate="A" pin="!INT"/>
<wire x1="58.42" y1="60.96" x2="63.5" y2="60.96" width="0.1524" layer="91"/>
<pinref part="R3" gate="A" pin="2"/>
<wire x1="68.58" y1="78.74" x2="63.5" y2="78.74" width="0.1524" layer="91"/>
<wire x1="63.5" y1="78.74" x2="63.5" y2="68.58" width="0.1524" layer="91"/>
<wire x1="63.5" y1="68.58" x2="63.5" y2="60.96" width="0.1524" layer="91"/>
<wire x1="81.28" y1="68.58" x2="63.5" y2="68.58" width="0.1524" layer="91"/>
<junction x="63.5" y="68.58"/>
<label x="81.28" y="68.58" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="INT" gate="G$1" pin="1"/>
<wire x1="-139.7" y1="5.08" x2="-139.7" y2="17.78" width="0.1524" layer="91"/>
<wire x1="-139.7" y1="17.78" x2="-142.24" y2="17.78" width="0.1524" layer="91"/>
<label x="-142.24" y="17.78" size="1.778" layer="95"/>
</segment>
</net>
<net name="V+" class="0">
<segment>
<pinref part="R3" gate="A" pin="1"/>
<wire x1="81.28" y1="78.74" x2="83.82" y2="78.74" width="0.1524" layer="91"/>
<wire x1="83.82" y1="78.74" x2="83.82" y2="81.28" width="0.1524" layer="91"/>
<pinref part="P+1" gate="1" pin="V+"/>
</segment>
<segment>
<pinref part="U1" gate="A" pin="VLED+"/>
<wire x1="58.42" y1="45.72" x2="71.12" y2="45.72" width="0.1524" layer="91"/>
<pinref part="U1" gate="A" pin="VLED+_2"/>
<wire x1="71.12" y1="45.72" x2="76.2" y2="45.72" width="0.1524" layer="91"/>
<wire x1="58.42" y1="40.64" x2="71.12" y2="40.64" width="0.1524" layer="91"/>
<wire x1="71.12" y1="45.72" x2="71.12" y2="40.64" width="0.1524" layer="91"/>
<junction x="71.12" y="45.72"/>
<pinref part="P+2" gate="1" pin="V+"/>
<wire x1="71.12" y1="40.64" x2="78.74" y2="40.64" width="0.1524" layer="91"/>
<junction x="71.12" y="40.64"/>
<pinref part="C2" gate="A" pin="1"/>
<wire x1="78.74" y1="40.64" x2="78.74" y2="38.1" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="R4" gate="A" pin="2"/>
<pinref part="P+3" gate="1" pin="V+"/>
<wire x1="-144.78" y1="68.58" x2="-149.86" y2="68.58" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="R5" gate="A" pin="2"/>
<wire x1="-144.78" y1="45.72" x2="-149.86" y2="45.72" width="0.1524" layer="91"/>
<pinref part="P+4" gate="1" pin="V+"/>
</segment>
<segment>
<pinref part="U2" gate="A" pin="VCC"/>
<wire x1="-119.38" y1="53.34" x2="-119.38" y2="45.72" width="0.1524" layer="91"/>
<pinref part="C6" gate="A" pin="1"/>
<wire x1="-119.38" y1="45.72" x2="-119.38" y2="38.1" width="0.1524" layer="91"/>
<wire x1="-111.76" y1="40.64" x2="-111.76" y2="45.72" width="0.1524" layer="91"/>
<wire x1="-111.76" y1="45.72" x2="-119.38" y2="45.72" width="0.1524" layer="91"/>
<junction x="-119.38" y="45.72"/>
<pinref part="P+5" gate="1" pin="V+"/>
</segment>
<segment>
<pinref part="U3" gate="A" pin="IN"/>
<wire x1="-60.96" y1="-5.08" x2="-60.96" y2="0" width="0.1524" layer="91"/>
<pinref part="C3" gate="A" pin="2"/>
<wire x1="-60.96" y1="0" x2="-63.5" y2="0" width="0.1524" layer="91"/>
<wire x1="-60.96" y1="0" x2="-60.96" y2="7.62" width="0.1524" layer="91"/>
<junction x="-60.96" y="0"/>
<pinref part="P+6" gate="1" pin="V+"/>
</segment>
<segment>
<pinref part="U3" gate="A" pin="!SHDN"/>
<wire x1="-60.96" y1="-10.16" x2="-60.96" y2="-15.24" width="0.1524" layer="91"/>
<pinref part="P+7" gate="1" pin="V+"/>
</segment>
<segment>
<pinref part="V+" gate="G$1" pin="1"/>
<wire x1="-124.46" y1="5.08" x2="-124.46" y2="17.78" width="0.1524" layer="91"/>
<wire x1="-124.46" y1="17.78" x2="-127" y2="17.78" width="0.1524" layer="91"/>
<label x="-127" y="17.78" size="1.778" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="U1" gate="A" pin="GND"/>
<wire x1="58.42" y1="55.88" x2="60.96" y2="55.88" width="0.1524" layer="91"/>
<pinref part="GND1" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="C1" gate="A" pin="2"/>
<wire x1="81.28" y1="55.88" x2="83.82" y2="55.88" width="0.1524" layer="91"/>
<pinref part="GND2" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="C2" gate="A" pin="2"/>
<pinref part="GND3" gate="1" pin="GND"/>
<wire x1="78.74" y1="27.94" x2="78.74" y2="30.48" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="U1" gate="A" pin="PGND"/>
<wire x1="-2.54" y1="50.8" x2="-7.62" y2="50.8" width="0.1524" layer="91"/>
<pinref part="GND4" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="C7" gate="A" pin="2"/>
<wire x1="-66.04" y1="33.02" x2="-66.04" y2="30.48" width="0.1524" layer="91"/>
<pinref part="GND5" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="U2" gate="A" pin="GND"/>
<wire x1="-119.38" y1="60.96" x2="-121.92" y2="60.96" width="0.1524" layer="91"/>
<wire x1="-121.92" y1="60.96" x2="-121.92" y2="63.5" width="0.1524" layer="91"/>
<pinref part="GND6" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="C6" gate="A" pin="2"/>
<wire x1="-111.76" y1="33.02" x2="-111.76" y2="30.48" width="0.1524" layer="91"/>
<pinref part="GND7" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="C3" gate="A" pin="1"/>
<wire x1="-71.12" y1="0" x2="-73.66" y2="0" width="0.1524" layer="91"/>
<pinref part="GND8" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="U3" gate="A" pin="AGND"/>
<pinref part="GND9" gate="1" pin="GND"/>
<wire x1="-60.96" y1="-7.62" x2="-63.5" y2="-7.62" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="U3" gate="A" pin="PGND"/>
<wire x1="-5.08" y1="-7.62" x2="-2.54" y2="-7.62" width="0.1524" layer="91"/>
<pinref part="GND10" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="C4" gate="A" pin="2"/>
<wire x1="45.72" y1="-5.08" x2="48.26" y2="-5.08" width="0.1524" layer="91"/>
<pinref part="GND11" gate="1" pin="GND"/>
</segment>
<segment>
<pinref part="GND" gate="G$1" pin="1"/>
<wire x1="-132.08" y1="-17.78" x2="-119.38" y2="-17.78" width="0.1524" layer="91"/>
<label x="-119.38" y="-17.78" size="1.778" layer="95"/>
</segment>
</net>
<net name="1.8V" class="0">
<segment>
<pinref part="U1" gate="A" pin="VDD"/>
<wire x1="58.42" y1="50.8" x2="71.12" y2="50.8" width="0.1524" layer="91"/>
<wire x1="71.12" y1="50.8" x2="83.82" y2="50.8" width="0.1524" layer="91"/>
<wire x1="71.12" y1="50.8" x2="71.12" y2="55.88" width="0.1524" layer="91"/>
<junction x="71.12" y="50.8"/>
<pinref part="C1" gate="A" pin="1"/>
<wire x1="71.12" y1="55.88" x2="73.66" y2="55.88" width="0.1524" layer="91"/>
<label x="83.82" y="50.8" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="R2" gate="A" pin="2"/>
<wire x1="-35.56" y1="68.58" x2="-40.64" y2="68.58" width="0.1524" layer="91"/>
<label x="-43.18" y="68.58" size="1.778" layer="95" rot="R180" xref="yes"/>
<label x="-43.18" y="68.58" size="1.778" layer="95" rot="R180" xref="yes"/>
<label x="-43.18" y="68.58" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
<segment>
<pinref part="R1" gate="A" pin="2"/>
<wire x1="-35.56" y1="48.26" x2="-40.64" y2="48.26" width="0.1524" layer="91"/>
<label x="-43.18" y="48.26" size="1.778" layer="95" rot="R180" xref="yes"/>
</segment>
<segment>
<pinref part="U2" gate="A" pin="!TS"/>
<wire x1="-58.42" y1="60.96" x2="-55.88" y2="60.96" width="0.1524" layer="91"/>
<wire x1="-55.88" y1="60.96" x2="-55.88" y2="63.5" width="0.1524" layer="91"/>
<label x="-55.88" y="63.5" size="1.778" layer="95" rot="R90" xref="yes"/>
</segment>
<segment>
<pinref part="U2" gate="A" pin="VL"/>
<wire x1="-58.42" y1="53.34" x2="-58.42" y2="45.72" width="0.1524" layer="91"/>
<wire x1="-58.42" y1="45.72" x2="-58.42" y2="40.64" width="0.1524" layer="91"/>
<wire x1="-58.42" y1="45.72" x2="-66.04" y2="45.72" width="0.1524" layer="91"/>
<junction x="-58.42" y="45.72"/>
<pinref part="C7" gate="A" pin="1"/>
<wire x1="-66.04" y1="45.72" x2="-66.04" y2="40.64" width="0.1524" layer="91"/>
<label x="-58.42" y="40.64" size="1.778" layer="95" xref="yes"/>
</segment>
<segment>
<pinref part="C5" gate="A" pin="2"/>
<wire x1="20.32" y1="-20.32" x2="35.56" y2="-20.32" width="0.1524" layer="91"/>
<wire x1="35.56" y1="-20.32" x2="35.56" y2="-22.86" width="0.1524" layer="91"/>
<pinref part="L1" gate="G$1" pin="2"/>
<pinref part="C4" gate="A" pin="1"/>
<wire x1="35.56" y1="-5.08" x2="38.1" y2="-5.08" width="0.1524" layer="91"/>
<wire x1="35.56" y1="-20.32" x2="35.56" y2="-5.08" width="0.1524" layer="91"/>
<junction x="35.56" y="-20.32"/>
<junction x="35.56" y="-5.08"/>
<label x="35.56" y="-22.86" size="1.778" layer="95" xref="yes"/>
</segment>
</net>
<net name="SDA" class="0">
<segment>
<pinref part="U2" gate="A" pin="IOVCC1"/>
<wire x1="-119.38" y1="58.42" x2="-132.08" y2="58.42" width="0.1524" layer="91"/>
<wire x1="-132.08" y1="58.42" x2="-132.08" y2="68.58" width="0.1524" layer="91"/>
<junction x="-132.08" y="58.42"/>
<pinref part="R4" gate="A" pin="1"/>
<wire x1="-167.64" y1="60.96" x2="-167.64" y2="58.42" width="0.1524" layer="91"/>
<wire x1="-167.64" y1="58.42" x2="-132.08" y2="58.42" width="0.1524" layer="91"/>
<label x="-167.64" y="60.96" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="SDA" gate="G$1" pin="1"/>
<wire x1="-124.46" y1="-5.08" x2="-114.3" y2="-5.08" width="0.1524" layer="91"/>
<label x="-114.3" y="-5.08" size="1.778" layer="95"/>
</segment>
</net>
<net name="SCL" class="0">
<segment>
<pinref part="U2" gate="A" pin="IOVCC2"/>
<wire x1="-119.38" y1="55.88" x2="-132.08" y2="55.88" width="0.1524" layer="91"/>
<wire x1="-132.08" y1="55.88" x2="-132.08" y2="45.72" width="0.1524" layer="91"/>
<junction x="-132.08" y="55.88"/>
<pinref part="R5" gate="A" pin="1"/>
<wire x1="-167.64" y1="53.34" x2="-167.64" y2="55.88" width="0.1524" layer="91"/>
<wire x1="-167.64" y1="55.88" x2="-132.08" y2="55.88" width="0.1524" layer="91"/>
<label x="-167.64" y="50.8" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="SCL" gate="G$1" pin="1"/>
<wire x1="-139.7" y1="-5.08" x2="-149.86" y2="-5.08" width="0.1524" layer="91"/>
<label x="-149.86" y="-5.08" size="1.778" layer="95"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="U3" gate="A" pin="LX"/>
<pinref part="L1" gate="G$1" pin="1"/>
<wire x1="-5.08" y1="-5.08" x2="20.32" y2="-5.08" width="0.1524" layer="91"/>
<pinref part="R6" gate="A" pin="1"/>
<wire x1="17.78" y1="-10.16" x2="20.32" y2="-10.16" width="0.1524" layer="91"/>
<wire x1="20.32" y1="-10.16" x2="20.32" y2="-5.08" width="0.1524" layer="91"/>
<junction x="20.32" y="-5.08"/>
</segment>
</net>
<net name="N$7" class="0">
<segment>
<pinref part="U3" gate="A" pin="OUT"/>
<pinref part="R6" gate="A" pin="2"/>
<wire x1="-5.08" y1="-10.16" x2="-2.54" y2="-10.16" width="0.1524" layer="91"/>
<wire x1="-2.54" y1="-10.16" x2="5.08" y2="-10.16" width="0.1524" layer="91"/>
<wire x1="-2.54" y1="-10.16" x2="-2.54" y2="-20.32" width="0.1524" layer="91"/>
<junction x="-2.54" y="-10.16"/>
<pinref part="C5" gate="A" pin="1"/>
<wire x1="-2.54" y1="-20.32" x2="12.7" y2="-20.32" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
<compatibility>
<note version="8.2" severity="warning">
Since Version 8.2, EAGLE supports online libraries. The ids
of those online libraries will not be understood (or retained)
with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports URNs for individual library
assets (packages, symbols, and devices). The URNs of those assets
will not be understood (or retained) with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports the association of 3D packages
with devices in libraries, schematics, and board files. Those 3D
packages will not be understood (or retained) with this version.
</note>
</compatibility>
</eagle>
