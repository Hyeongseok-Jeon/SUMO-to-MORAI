// Generated by gencpp from file morai_msgs/GhostMessage.msg
// DO NOT EDIT!


#ifndef MORAI_MSGS_MESSAGE_GHOSTMESSAGE_H
#define MORAI_MSGS_MESSAGE_GHOSTMESSAGE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Vector3.h>

namespace morai_msgs
{
template <class ContainerAllocator>
struct GhostMessage_
{
  typedef GhostMessage_<ContainerAllocator> Type;

  GhostMessage_()
    : position()
    , heading(0.0)  {
    }
  GhostMessage_(const ContainerAllocator& _alloc)
    : position(_alloc)
    , heading(0.0)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _position_type;
  _position_type position;

   typedef double _heading_type;
  _heading_type heading;





  typedef boost::shared_ptr< ::morai_msgs::GhostMessage_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::morai_msgs::GhostMessage_<ContainerAllocator> const> ConstPtr;

}; // struct GhostMessage_

typedef ::morai_msgs::GhostMessage_<std::allocator<void> > GhostMessage;

typedef boost::shared_ptr< ::morai_msgs::GhostMessage > GhostMessagePtr;
typedef boost::shared_ptr< ::morai_msgs::GhostMessage const> GhostMessageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::morai_msgs::GhostMessage_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::morai_msgs::GhostMessage_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::morai_msgs::GhostMessage_<ContainerAllocator1> & lhs, const ::morai_msgs::GhostMessage_<ContainerAllocator2> & rhs)
{
  return lhs.position == rhs.position &&
    lhs.heading == rhs.heading;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::morai_msgs::GhostMessage_<ContainerAllocator1> & lhs, const ::morai_msgs::GhostMessage_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace morai_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::morai_msgs::GhostMessage_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::morai_msgs::GhostMessage_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::morai_msgs::GhostMessage_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::morai_msgs::GhostMessage_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::morai_msgs::GhostMessage_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::morai_msgs::GhostMessage_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::morai_msgs::GhostMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b7529b96025c54855f296c4413ac7578";
  }

  static const char* value(const ::morai_msgs::GhostMessage_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb7529b96025c5485ULL;
  static const uint64_t static_value2 = 0x5f296c4413ac7578ULL;
};

template<class ContainerAllocator>
struct DataType< ::morai_msgs::GhostMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "morai_msgs/GhostMessage";
  }

  static const char* value(const ::morai_msgs::GhostMessage_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::morai_msgs::GhostMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/Vector3 position\n"
"\n"
"float64 heading\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::morai_msgs::GhostMessage_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::morai_msgs::GhostMessage_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.position);
      stream.next(m.heading);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GhostMessage_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::morai_msgs::GhostMessage_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::morai_msgs::GhostMessage_<ContainerAllocator>& v)
  {
    s << indent << "position: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.position);
    s << indent << "heading: ";
    Printer<double>::stream(s, indent + "  ", v.heading);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MORAI_MSGS_MESSAGE_GHOSTMESSAGE_H
