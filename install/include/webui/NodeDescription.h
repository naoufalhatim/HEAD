// Generated by gencpp from file webui/NodeDescription.msg
// DO NOT EDIT!


#ifndef WEBUI_MESSAGE_NODEDESCRIPTION_H
#define WEBUI_MESSAGE_NODEDESCRIPTION_H

#include <ros/service_traits.h>


#include <webui/NodeDescriptionRequest.h>
#include <webui/NodeDescriptionResponse.h>


namespace webui
{

struct NodeDescription
{

typedef NodeDescriptionRequest Request;
typedef NodeDescriptionResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct NodeDescription
} // namespace webui


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::webui::NodeDescription > {
  static const char* value()
  {
    return "02f6d2fdd12a11088c4d10303fc40b3c";
  }

  static const char* value(const ::webui::NodeDescription&) { return value(); }
};

template<>
struct DataType< ::webui::NodeDescription > {
  static const char* value()
  {
    return "webui/NodeDescription";
  }

  static const char* value(const ::webui::NodeDescription&) { return value(); }
};


// service_traits::MD5Sum< ::webui::NodeDescriptionRequest> should match 
// service_traits::MD5Sum< ::webui::NodeDescription > 
template<>
struct MD5Sum< ::webui::NodeDescriptionRequest>
{
  static const char* value()
  {
    return MD5Sum< ::webui::NodeDescription >::value();
  }
  static const char* value(const ::webui::NodeDescriptionRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::webui::NodeDescriptionRequest> should match 
// service_traits::DataType< ::webui::NodeDescription > 
template<>
struct DataType< ::webui::NodeDescriptionRequest>
{
  static const char* value()
  {
    return DataType< ::webui::NodeDescription >::value();
  }
  static const char* value(const ::webui::NodeDescriptionRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::webui::NodeDescriptionResponse> should match 
// service_traits::MD5Sum< ::webui::NodeDescription > 
template<>
struct MD5Sum< ::webui::NodeDescriptionResponse>
{
  static const char* value()
  {
    return MD5Sum< ::webui::NodeDescription >::value();
  }
  static const char* value(const ::webui::NodeDescriptionResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::webui::NodeDescriptionResponse> should match 
// service_traits::DataType< ::webui::NodeDescription > 
template<>
struct DataType< ::webui::NodeDescriptionResponse>
{
  static const char* value()
  {
    return DataType< ::webui::NodeDescription >::value();
  }
  static const char* value(const ::webui::NodeDescriptionResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // WEBUI_MESSAGE_NODEDESCRIPTION_H