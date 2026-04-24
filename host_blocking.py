from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

packet_count = {}
THRESHOLD = 10

def _handle_PacketIn(event):
    packet = event.parsed
    in_port = event.port
    dpid = event.connection.dpid

    key = (dpid, in_port)
    packet_count[key] = packet_count.get(key, 0) + 1

    log.info("Port %s count: %s" % (in_port, packet_count[key]))

    # Block traffic if threshold exceeded
    if packet_count[key] > THRESHOLD:
        log.info("Blocking port %s" % in_port)

        msg = of.ofp_flow_mod()
        msg.match.in_port = in_port
        msg.priority = 100
        msg.actions = []  # DROP

        event.connection.send(msg)
        return

    # Allow normal traffic (flood)
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.in_port = in_port
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

    event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("POX Firewall Controller Running")
