from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.connection.dpid

    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    mac_to_port[dpid][packet.src] = event.port

    if packet.dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][packet.dst]
    else:
        out_port = of.OFPP_FLOOD

    actions = [of.ofp_action_output(port=out_port)]

    # Install flow
    flow = of.ofp_flow_mod()
    flow.match = of.ofp_match.from_packet(packet)
    flow.actions = actions
    flow.idle_timeout = 10
    flow.hard_timeout = 30
    event.connection.send(flow)

    # Forward current packet
    packet_out = of.ofp_packet_out()
    packet_out.data = event.ofp
    packet_out.actions = actions
    packet_out.in_port = event.port
    event.connection.send(packet_out)

    log.info("Flow installed and packet forwarded")

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("🔥 Orange Project Controller Running")
